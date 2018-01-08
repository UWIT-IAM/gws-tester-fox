# create a gws group, put, get, compare

from copy import deepcopy
import json
import time
import urllib3
import settings as conf

put_headers = {"Content-type": "application/json"}
get_headers = {"Accept": "application/json"}

start_time = time.time()

http = None


def _get_pool_manager():
    global http
    if http is None:
        http = urllib3.PoolManager(cert_file=conf.CERT_FILE,
                                   key_file=conf.KEY_FILE,
                                   ca_certs=conf.CA_FILE,
                                   cert_reqs='CERT_REQUIRED')


def build_group(conf_group):

    group = deepcopy(conf_group)
    url = conf.GWS_BASE + '/group/' + group['id']
    print('PUT: ' + url)
    pgroup = {}
    pgroup['data'] = group
    data = json.dumps(pgroup)
    # print('json: ' + data)

    _get_pool_manager()
    resp = http.request('PUT', url, headers=put_headers, body=data)

    print(resp.status)
    # print(resp.data)
    if resp.status != 201:
        print('put of testgroup failed')
    return resp.status


def _verify_admin(conf_group, data, type):
    if type in conf_group:
        admins = data[type]
        assert len(admins) == len(conf_group[type])
        # note the entries are not sorted
        for i in range(0, len(admins)):
            match = -1
            for j in range(0, len(conf_group[type])):
                if admins[i]['type'] == conf_group[type][j]['type'] and admins[i]['id'] == conf_group[type][j]['id']:
                    match = j
            assert match >= 0
    else:
        if type == 'readers':
            assert(data[type][0]['type'] == 'set')
            assert(data[type][0]['id'] == 'all')
        else:
            assert len(data[type]) == 0


def group_status(conf_group):
    url = conf.GWS_BASE + '/group/' + conf_group['id']
    print('GET: ' + url)
    ret = 0
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        ret = resp.status
    except json.decoder.JSONDecodeError:
        print('invalid json in gws group response')
        return 599
    return ret


def verify_group(conf_group, conf_aff=None):
    url = conf.GWS_BASE + '/group/' + conf_group['id']
    print('GET: ' + url)
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        # print(resp.data)

        group = json.loads(resp.data.decode("utf-8"))

        # meta stuff
        assert group['schemas'][0] == conf.SCHEMA
        meta = group['meta']
        assert meta['resourceType'] == 'group'
        assert meta['selfRef'] == url
        assert meta['memberRef'] == url + '/member/'

        data = group['data']
        assert len(data['regid']) == 32
        assert data['id'] == conf_group['id']
        assert data['displayName'] == conf_group['displayName']
        assert data['description'] == conf_group['description']
        assert int(data['created'])/1000 > start_time
        assert int(data['lastModified'])/1000 > start_time
        assert int(data['lastMemberModified']) == 0
        assert data['authnFactor'] == conf_group['authnfactor']
        assert data['classification'] == conf_group['classification']
        assert data['dependsOn'] == ''
        assert data['contact'] == conf_group['contact']
        assert int(data['gid']) > 0

        _verify_admin(conf_group, data, 'admins')
        _verify_admin(conf_group, data, 'updaters')
        _verify_admin(conf_group, data, 'creators')
        _verify_admin(conf_group, data, 'readers')
        _verify_admin(conf_group, data, 'optins')
        _verify_admin(conf_group, data, 'optouts')

        if conf_aff is not None:
            for aff in data['affiliates']:
                if aff['name'] == conf_aff['name']:
                    print('verify ' + aff['name'])
                    _verify_senders(aff, conf_aff)

    except json.decoder.JSONDecodeError:
        print('invalid json in gws group response')
        return 599

    return 200


def delete_group(conf_group):
    url = conf.GWS_BASE + '/group/' + conf_group['id']
    print('DEL: ' + url)
    _get_pool_manager()
    resp = http.request('DELETE', url, headers=get_headers)
    print(resp.status)
    return resp.status


def add_members(conf_group, members):

    mbrs = []
    for mbr in members:
        mbrs.append(mbr['id'])
    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/member/' + ','.join(mbrs) + '?synchronized'
    print('PUT: ' + url)
    _get_pool_manager()
    resp = http.request('PUT', url, headers=put_headers, body=None)

    print(resp.status)
    # print(resp.data)
    if resp.status != 200:
        print('put of members failed')
    return resp.status


def set_membership(conf_group, members):

    pmembers = {}
    pmembers['data'] = members
    data = json.dumps(pmembers)
    # print('json: ' + data)
    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/member/' + '?synchronized'
    print('PUT: ' + url)
    _get_pool_manager()
    resp = http.request('PUT', url, headers=put_headers, body=data)

    print(resp.status)
    # print(resp.data)
    if resp.status != 200:
        print('put of members failed')
    return resp.status


def verify_members(conf_group, conf_members):
    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/member/'
    print('verify GET: ' + url)
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        print(resp.data)
        member_res = json.loads(resp.data.decode("utf-8"))

        for gmbr in member_res['data']:
            print(gmbr)
            match = -1
            for cmbr in conf_members:
                if gmbr['type'] == cmbr['type'] and gmbr['id'] == cmbr['id']:
                    match = 1
            assert match >= 0

    except json.decoder.JSONDecodeError:
        print('invalid json in gws member response')
        print(resp.data)
        return 599

    return 200


def put_affiliate(conf_group, conf_aff):

    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/affiliate/' + conf_aff['name'] + \
                          '?status=' + conf_aff['status'] + '&sender=' + ','.join(conf_aff['senders'])
    print('PUT: ' + url)

    _get_pool_manager()
    resp = http.request('PUT', url, headers=put_headers, body=None)

    print(resp.status)
    # print(resp.data)
    if resp.status != 200 and resp.status != 201:
        print('put of affiliate failed')
    return resp.status


def _verify_senders(data, conf_aff):
    for sndr in data['senders']:
        print(sndr)
        if sndr['type'] == 'set' and sndr['id'] == 'all':
            sndr['id'] = 'dc=all'
        match = -1
        for csndr in conf_aff['senders']:
            if sndr['id'] == csndr:
                match = 1
        assert match >= 0


def verify_affiliate(conf_group, conf_aff):
    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/affiliate/' + conf_aff['name']
    print('verify GET: ' + url)
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        print(resp.data)
        aff_res = json.loads(resp.data.decode("utf-8"))

        # meta stuff
        assert aff_res['schemas'][0] == conf.SCHEMA
        meta = aff_res['meta']
        assert meta['resourceType'] == 'affiliate'
        assert meta['selfRef'] == url

        data = aff_res['data']
        assert(data['name']) == conf_aff['name']
        assert(data['status']) == conf_aff['status']
        _verify_senders(data, conf_aff)

    except json.decoder.JSONDecodeError:
        print('invalid json in get affiliate response')
        print(resp.data)
        return 599

    return 200


def verify_history(conf_group, min_items=1):
    url = conf.GWS_BASE + '/group/' + conf_group['id'] + '/history/'
    print('GET: ' + url)
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        # print(resp.data)

        group = json.loads(resp.data.decode("utf-8"))

        # meta stuff
        assert group['schemas'][0] == conf.SCHEMA
        meta = group['meta']
        assert meta['resourceType'] == 'history'
        assert meta['selfRef'] == url

        data = group['data']

        assert len(data) > min_items

    except json.decoder.JSONDecodeError:
        print('invalid json in get affiliate response')
        print(resp.data)
        return 599

    return 200


def search_groups(member=None, stem=None, name=None, scope=None, type=None):
    url = conf.GWS_BASE + '/search'
    sep = '?'
    if member is not None:
        url = url + sep + 'member=' + member
        sep = '&'
    if name is not None:
        url = url + sep + 'name=' + name
        sep = '&'
    if stem is not None:
        url = url + sep + 'stem=' + stem
        sep = '&'
    if scope is not None:
        url = url + sep + 'scope=' + scope
        sep = '&'
    if type is not None:
        url = url + sep + 'type=' + type
        sep = '&'

    print('GET: ' + url)
    _get_pool_manager()
    data = None
    status = 200
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        status = resp.status
        # print(resp.data)

        content = json.loads(resp.data.decode("utf-8"))

        # meta stuff
        assert content['schemas'][0] == conf.SCHEMA
        meta = content['meta']
        assert meta['resourceType'] == 'search'
        # assert meta['selfRef'] == url
        data = content['data']

    except json.decoder.JSONDecodeError:
        print('invalid json in get affiliate response')
        print(resp.data)
        status = 599

    return (status, data)
