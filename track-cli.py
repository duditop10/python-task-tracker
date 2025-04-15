import datetime
import argparse
import json
import os
taskFilePath='C:\\cli-tools\\track-cli.json'
def loadFile():
    if os.path.exists(taskFilePath):
        with open(taskFilePath, "r") as f:
            return json.load(f)
    else:
        with open(taskFilePath, "x") as f:
            return[]
        
def saveFile(tasks):
    with open(taskFilePath, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks=loadFile()
    parser = argparse.ArgumentParser(description='Simple task tracker made in python.')
    subparsers = parser.add_subparsers(dest='command')
    add=subparsers.add_parser('add', help='Adds task to to-do list.')
    add.add_argument('task', help='The description of the task you are adding.')
    update=subparsers.add_parser('update', help='Changes description of task.')
    update.add_argument('id', type=int, help='Numerical id of the task you want to update.')
    update.add_argument('updatedTask', help='The updated description of the task.')
    delete=subparsers.add_parser('delete', help='Deletes task.')
    delete.add_argument('id', type=int, help='Numerical id of task you want to delete.')
    mark_to_do=subparsers.add_parser('mark-to-do', help='Marks task as to-do.')
    mark_to_do.add_argument('id', type=int, help='Numerical id of task you want to mark as to-do.')
    mark_in_progress=subparsers.add_parser('mark-in-progress', help='Marks task as in progress.')
    mark_in_progress.add_argument('id', type=int, help='Numerical id of task you want to mark as in progress.')
    mark_done=subparsers.add_parser('mark-done', help='Marks task as done.')
    mark_done.add_argument('id', type=int, help='Numerical id of task you want to mark as in done.')
    list=subparsers.add_parser('list', help='Lists tasks filtered by status (to-do, in progress, done, not done and all). By default lists all.')
    list.add_argument('status',nargs='?',default='all',choices=['to-do','done','in-progress','not-done','all'], help="The status by which you're filtering the tasks listed.")
    args=parser.parse_args()
    if args.command=='add':
        lastId=0;
        if len(tasks)!=0:
            lastId=tasks[-1]['id']
        taskId=lastId+1
        createdAt=str(datetime.datetime.now())
        task={'id':taskId,'description':args.task,'status':'to-do','createdAt':createdAt,'updatedAt':createdAt}
        tasks.append(task)
        saveFile(tasks)
        print(f'"{task['description']}" was added')
    elif args.command=='update':
        foundTask=False
        for task in tasks:
            if task['id']==args.id:
                foundTask=True
                oldDescription = task['description']
                task['description']=args.updatedTask
                task['updatedAt']=str(datetime.datetime.now())
                saveFile(tasks)
                print(f'"{oldDescription}" was updated to "{task['description']}"')
        if foundTask == False:
            print("Error: No such ID found")
    elif args.command=='delete':
        foundTask=False
        for task in tasks:
            if task['id']==args.id:
                taskDescription=task['description']
                tasks.remove(task)
                saveFile(tasks)
                print(f'"{taskDescription}" was deleted')
        if foundTask == False:
            print("Error: No such ID found")
    elif args.command=='mark-to-do':
        foundTask=False
        for task in tasks:
            if task['id']==args.id:
                taskDescription=task['description']
                task['status']='to-do'
                saveFile(tasks)
                print(f'"{taskDescription}" status changed to to-do')
        if foundTask == False:
            print("Error: No such ID found")
    elif args.command=='mark-in-progress':
        foundTask=False
        for task in tasks:
            if task['id']==args.id:
                taskDescription=task['description']
                task['status']='in progress'
                saveFile(tasks)
                print(f'"{taskDescription}" status changed to in progress')
        if foundTask == False:
            print("Error: No such ID found")
    elif args.command=='mark-done':
        foundTask=False
        for task in tasks:
            if task['id']==args.id:
                taskDescription=task['description']
                task['status']='done'
                saveFile(tasks)
                print(f'"{taskDescription}" status changed to done')
        if foundTask == False:
            print("Error: No such ID found")
    elif args.command=='list':
        if args.status=='all':
            for task in tasks:
                print(f'ID:{task['id']}  ||  Task:{task['description']}  ||  Status:{task['status']}  ||  Created at:{task['createdAt']}  ||  Updated last:{task['updatedAt']}\n\n')
        elif args.status=='not-done':
            for task in tasks:
                if task['status']!='done':    
                    print(f'ID:{task['id']}  ||  Task:{task['description']}  ||  Status:{task['status']}  ||  Created at:{task['createdAt']}  ||  Updated last:{task['updatedAt']}\n\n')
        else:
            for task in tasks:
                if task['status'].replace('-',' ')==args.status.replace('-',' '):    
                    print(f'ID:{task['id']}  ||  Task:{task['description']}  ||  Status:{task['status']}  ||  Created at:{task['createdAt']}  ||  Updated last:{task['updatedAt']}\n\n')
            
if __name__=='__main__':
    main()