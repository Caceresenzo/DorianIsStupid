# pip install psutil
# pip install cmd2

import psutil
from cmd2 import Cmd
import time


class Utils:

    @staticmethod
    def printFormat(object):
        print('+' + ("-" * 72) + '+')

        if isinstance(object, list):
            for string in object:
                if string == '*-*':
                    print('+' + ("-" * 72) + '+')
                else:
                    print('| {:70} |'.format(string.replace('\t', ' ' * 4)))
        else:
            print('| {:70} |'.format(object.replace('\t', ' ' * 4)))

        print('+' + ("-" * 72) + '+')

    @staticmethod
    def isStringInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def formatProgressBar(pourcent):
        return '\t[{:_<50}] {}'.format('#' * int((pourcent / 100) * 50), str(pourcent) + '%')

    def byteToHuman(bytes, prescision = 2):
        if bytes < 1024:
            result = bytes + ' B'
        elif bytes < 1048576:
           return str(round((bytes / 1024), prescision)) + ' KB'
        elif (bytes < 1073741824):
            return str(round((bytes / 1048576), prescision)) + ' MB'
        else:
            return str(round((bytes / 1073741824), prescision)) + ' GB'


class SystemInfo (Cmd):
    prompt = 'command> '
    intro = Utils.printFormat('SystemInfo Command Interpreter')

    def __init__(self):
        Cmd.__init__(self)

    def do_help(self, line):
        output = list()

        output.append('STATUS CPU - Get usage of all cpu(s)')
        output.append('STATUS CPU {CPU ID} - Get usage of cpu id')
        output.append('STATUS CPU REALTIME - Get realtime updating of average processor usage')
        output.append('STATUS MEMORY - Get memory information')

        Utils.printFormat(output)

    def do_status(self, line):
        output = list()
        arguments = line.lower().split(' ')
        length = len(arguments)

        if length < 1:
            print('Need more argument')
            return

        if arguments[0] == 'cpu':
            cpuCount = psutil.cpu_count()
            cpuUsage = psutil.cpu_percent(percpu = True)

            if length == 1:
                output.append('Number of processor: ' + str(cpuCount))

                for processor in range(0, cpuCount):
                    output.append('Processor ' + str(processor + 1))
                    output.append(Utils.formatProgressBar(cpuUsage[processor]))
            elif length == 2:
                if arguments[1] == 'realtime':
                    while True:
                        cpuUsage = psutil.cpu_percent(interval = 1, percpu = True)
                        average = 0

                        total = 0
                        for processor in range(0, cpuCount):
                            total += cpuUsage[processor]

                        average = round(total / cpuCount, 1)
                        print(Utils.formatProgressBar(average) + (' ' * 10) + '\r', end = '')
                else:
                    if not Utils.isStringInt(arguments[1]):
                        print('CPU id must be an integer')
                        return
                    if int(arguments[1]) < 1:
                        print('Out of range, you only got ' + str(cpuCount) + ' cpu(s)')
                        return
                    if int(arguments[1]) > cpuCount:
                        print('Out of range, must be above 0')
                        return

                    processor = int(arguments[1]) - 1
                    output.append('Information for processor: ' + str(processor + 1))
                    output.append(Utils.formatProgressBar(cpuUsage[processor]))
        elif arguments[0] == 'memory':
            memoryRam = psutil.virtual_memory()
            memorySwap = psutil.swap_memory()

            output.append('Memory information: RAM')
            output.append(' ')
            # output.append('\tAvailable: ' + str(Utils.byteToHuman(memoryRam.available)))
            # output.append('\tUsed: ' + str(Utils.byteToHuman(memoryRam.used)))
            # output.append('\tFree: ' + str(Utils.byteToHuman(memoryRam.free)))
            # output.append('\tTotal: ' + str(Utils.byteToHuman(memoryRam.total)))
            output.append('\t{:^15} {:^15} {:^15} {:^15}'.format('Available', 'Used', 'Free', 'Total'))
            output.append('\t{:^15} {:^15} {:^15} {:^15}'.format(Utils.byteToHuman(memoryRam.available), Utils.byteToHuman(memoryRam.used), Utils.byteToHuman(memoryRam.free), Utils.byteToHuman(memoryRam.total)))
            output.append(Utils.formatProgressBar(memoryRam.percent))
            output.append('*-*')

            output.append('Memory information: SWAP')
            output.append(' ')
            output.append('\t{:^15} {:^15} {:^15}'.format('Used', 'Free', 'Total'))
            output.append('\t{:^15} {:^15} {:^15}'.format(Utils.byteToHuman(memorySwap.used), Utils.byteToHuman(memorySwap.free), Utils.byteToHuman(memorySwap.total)))
            output.append(Utils.formatProgressBar(memorySwap.percent))

        Utils.printFormat(output)

    def do_exit(self, line):
        Utils.printFormat('Good bye!')
        exit()


app = SystemInfo()
app.cmdloop()
