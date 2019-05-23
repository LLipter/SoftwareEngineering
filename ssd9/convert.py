from biplist import *

plist = readPlist("ku_ssd9.plist")
with open('ku_ssd9.txt', 'w') as file_question:
    with open('ku_ssd9_sol.txt', 'w') as file_solution:
        for question in plist:
            question['identifier'] = str(int(question['identifier']) - 1)

            # format question
            q = question['question'].strip()[len(question['identifier'])+1:]
            if(question['identifier'] == '138' or question['identifier'] == '139'):
                q = q[4:]
            if(question['identifier'] == '99'):
                q = q[2:]
            file_question.write(question['identifier'] + '. ')
            idx = q.find('/')
            while (idx != -1):
                file_question.write(q[:idx].strip() + '\n')
                q = q[idx:].strip('/')
                idx = q.find('/')
            file_question.write(q.strip() + '\n')

            # format options
            file_question.write('A. ' + question['optionA'].strip() + '\n')
            file_question.write('B. ' + question['optionB'].strip() + '\n')
            file_question.write('C. ' + question['optionC'].strip() + '\n')
            file_question.write('D. ' + question['optionD'].strip() + '\n')
            file_question.write('\n')
            
            # format answer
            file_solution.write(question['identifier'] + '. ')
            file_solution.write(question['answer'].upper())
            file_solution.write('\n')
            if(int(question['identifier']) % 5 == 0):
                file_solution.write('\n')