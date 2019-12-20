import requests


def nxapi_show_version():
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = "admin"
    switchpassword = "Admin_1234!"

    http_headers = {"Content-Type": "application/json-rpc"}
    payload = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "show version", "version": 1},
            "id": 1,
        }
    ]
    # 1. use requests to post to the switch
    # response = requests.get(url, data=json.dumps(payload), headers=http_headers,
    #                          auth=(switchuser, switchpassword), verify=False).json()

    # response = requests.post(url, data=json.dumps(payload), headers=http_headers,
    #                         auth=(switchuser, switchpassword), verify=False).json()

    response = requests.post(
        url,
        json=payload,
        # data=json.dumps(payload),
        headers=http_headers,
        auth=(switchuser, switchpassword),
        verify=False,
    )

    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }

    return response.json()["result"]["body"]["kickstart_ver_str"]


if __name__ == "__main__":
    result = nxapi_show_version()
    print(result)
