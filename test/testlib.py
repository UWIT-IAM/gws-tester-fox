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
    print('json: ' + data)

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


def verify_group(conf_group):
    url = conf.GWS_BASE + '/group/' + conf_group['id']
    print('GET: ' + url)
    _get_pool_manager()
    try:
        resp = http.request('GET', url, headers=get_headers)
        print(resp.status)
        # print(resp.data)

        group = json.loads(resp.data.decode("utf-8"))

        # meta stuff
        assert group['schemas'][0] == conf.SCHEMAS['group']
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
