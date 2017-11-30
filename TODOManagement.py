print 'Welcome to the TODO task management programm.'

todo_list = {}

while True:
    task = raw_input("Please enter a TODO tast: ")

    done = raw_input('Is the task done? (yes/no)')
    if done == 'yes':
        done = True
    else:
        done = False

    todo_list[task] = done

    new = raw_input('Would you like to enter new task? (yes/no)')

    if new == "no":
        break

# print "All tasks: %s" % todo_list
# print 'All tasks: {0}'.format(todo_list)
# print 'All tasks ', todo_list

print 'Incomplete tasks:'
for todo in todo_list:
    if todo_list[todo] == False:
        print todo

print 'Complete tasks:'
for todo in todo_list:
    if todo_list[todo] == True:
        print todo

print 'Writing to file...'

# oeffne die Datei zum lesen und schreiben(w+)
todo_file = open('todos.txt', 'w+')

todo_file.write('Incomplete tasks:\n')
for todo in todo_list:
    if todo_list[todo] == False:
        todo_file.write(todo)

todo_file.write('\n---------------\n')
todo_file.write('Complete tasks:\n')
for todo in todo_list:
    if todo_list[todo] == True:
        todo_file.write(todo)

todo_file.close()

print "END"
