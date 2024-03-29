from opcua import Client, ua
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
import sys, logging

class HelloClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()


if __name__ == '__main__':
    servAddr = sys.argv[1].replace("0.0.0.0", "localhost")
    #logging.basicConfig(level=logging.DEBUG)
    with HelloClient("opc.tcp://" + servAddr + "/freeopcua/server/") as client:
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)
        endpoints = client.get_endpoints()
        print("There are", len(endpoints), "endpoints")

        hellower = objects.get_child("0:Hellower")
        print("Hellower is: ", hellower)

        values = client.get_values([ hellower ])
        print("Hellower values are", values)

        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        value = myvar.get_value()
        print("myvar value is: ", value)
        myvar.set_value(3.9)
        value = myvar.get_value()
        print("myvar value set, is now: ", value)
        
        resulting_text = hellower.call_method("0:SayHello", False)
        print(resulting_text)

        resulting_text = hellower.call_method("1:SayHello2", True)
        print(resulting_text)

        resulting_array = hellower.call_method("1:SayHelloArray", False)
        print(resulting_array)

        #result = hellower.call_method("2:SayNothing", False)
        #print(result)