#!/usr/bin/env python

class OtherClassName(object):
    def method(self):
        return "Real Other Class method answer"

class ClassName(OtherClassName):
    @staticmethod
    def staticMethod():
        return "Real static method answer"

    @staticmethod
    def otherStaticMethod():
        return "Other Real static method answer"

    def __repr__(self):
        return "infofinder.ClassName()"
