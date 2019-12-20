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

    response = requests.post(
        url,
        json=payload,
        # data=json.dumps(payload),
        headers=http_headers,
        auth=(switchuser, switchpassword),
        verify=False,
    )

    return response.json()["result"]["body"]["kickstart_ver_str"]


if __name__ == "__main__":
    result = nxapi_show_version()
    print(result)
