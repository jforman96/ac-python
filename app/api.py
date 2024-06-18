from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
import requests

class AzerothCoreAPI:
    def __init__(self, url):
        self.url = url
        self.headers = {'content-type': 'text/xml'}


    def _create_soap_request(self, command):
        envelope = Element('SOAP-ENV:Envelope', {
            'xmlns:SOAP-ENV': "http://schemas.xmlsoap.org/soap/envelope/",
            'xmlns:SOAP-ENC': "http://schemas.xmlsoap.org/soap/encoding/",
            'xmlns:xsi': "http://www.w3.org/1999/XMLSchema-instance",
            'xmlns:xsd': "http://www.w3.org/1999/XMLSchema",
            'xmlns:ns1': "urn:AC"
        })


        body = SubElement(envelope, 'SOAP-ENV:Body')
        execute_command = SubElement(body, 'ns1:executeCommand')
        command_element = SubElement(execute_command, 'command')
        command_element.text = command
        raw_xml = tostring(envelope, 'utf-8')
        pretty_xml = parseString(raw_xml).toprettyxml()

        return pretty_xml


    def execute_command(self, command):
        soap_request = self._create_soap_request(command)
        response = requests.post(self.url, data=soap_request, headers=self.headers)
        soup = BeautifulSoup(response.content, 'lxml-xml')
        result_element = soup.find('result')

        if result_element is not None:
            result = result_element.text
        else:
            fault_element = soup.find('faultstring')
            if fault_element is not None:
                result = "SOAP Error: " + fault_element.text
            else:
                result = "Result element not found"

        return result


    # AC functions
    def account(self, sub_command, *args):
        command = f'.account {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def character(self, sub_command, *args):
        command = f'.character {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def guild(self, sub_command, *args):
        command = f'.guild {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def go(self, sub_command, *args):
        command = f'.go {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def gm(self, sub_command, *args):
        command = f'.gm {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def modify(self, sub_command, *args):
        command = f'.modify {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def npc(self, sub_command, *args):
        command = f'.npc {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def quest(self, sub_command, *args):
        command = f'.quest {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def reload(self, sub_command, *args):
        command = f'.reload {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def reset(self, sub_command, *args):
        command = f'.reset {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def server(self, sub_command, *args):
        command = f'.server {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def teleport(self, sub_command, *args):
        command = f'.teleport {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def title(self, sub_command, *args):
        command = f'.title {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def unban(self, sub_command, *args):
        command = f'.unban {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def wchange(self, sub_command, *args):
        command = f'.wchange {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def achievement(self, sub_command, *args):
        command = f'.achievement {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)
    

    def ban(self, sub_command, *args):
        command = f'.ban {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def kick(self, sub_command, *args):
        command = f'.kick {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)


    def mute(self, sub_command, *args):
        command = f'.mute {sub_command} {" ".join(str(arg) for arg in args)}'
        return self.execute_command(command)

