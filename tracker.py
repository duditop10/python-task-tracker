#!/usr/bin/env python
import cmd

class TrackCLI(cmd.Cmd):
    prompt=">> "
    intro="Welcome to python task tracker. Type 'help' for available commands"
    def do_update(self,id):
        """Update existing item in to-do list"""
        print("Updating thing with id: "+id)
    def do_quit(self,line):
        """Exit CLI"""
        return True
    pass

if __name__=="__main__":
    TrackCLI().cmdloop()
