import os.path, logging
from opcua import ua, uamethod, Server


@uamethod
def say_hello_xml(parent, happy):
    print("Calling say_hello_xml")
    if happy:
        result = "I'm happy"
    else:
        result = "I'm not happy"
    print(result)
    return result


@uamethod
def say_hello(parent, happy):
    if happy:
        result = "I'm happy"
    else:
        result = "I'm not happy"
    print(result)
    return result


@uamethod
def say_hello_array(parent, happy):
    if happy:
        result = "I'm happy"
    else:
        result = "I'm not happy"
    print(result)
    return [result, "Actually I am"]


class HelloServer:
    def __init__(self, endpoint, name, model_filepath):
        self.server = Server()

        #  This need to be imported at the start or else it will overwrite the data
        self.server.import_xml(model_filepath)

        self.server.set_endpoint(endpoint)
        self.server.set_server_name(name)

        objects = self.server.get_objects_node()

        freeopcua_namespace = self.server.get_namespace_index("urn:freeopcua:python:server")
        hellower = objects.get_child("0:Hellower")
        hellower_say_hello = hellower.get_child("0:SayHello")

        self.server.link_method(hellower_say_hello, say_hello_xml)

        hellower.add_method(
            freeopcua_namespace, "SayHello2", say_hello, [ua.VariantType.Boolean], [ua.VariantType.String])

        hellower.add_method(
            freeopcua_namespace, "SayHelloArray", say_hello_array, [ua.VariantType.Boolean], [ua.VariantType.String])
        
        # setup our own namespace, not really necessary but should as spec
        uri = "http://examples.freeopcua.github.io"
        idx = self.server.register_namespace(uri)
        
        myobj = objects.add_object(idx, "MyObject")
        myvar = myobj.add_variable(idx, "MyVariable", 6.7)
        myvar.set_writable()    # Set MyVariable to be writable by clients

    def start(self):
        self.server.start()

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    logger_ignore = logging.getLogger("opcua.server.server")
    logger_ignore.setLevel(logging.ERROR)
    server = HelloServer(
                "opc.tcp://0.0.0.0:0/freeopcua/server/",
                "FreeOpcUa Example Server",
                os.path.join(script_dir, "test_saying.xml"))
    server.start()
