from pwn import *
from subprocess import Popen, PIPE
from json import loads
from time import sleep

socket = remote('nc.ctf.yummytacos.me', 10528)
field = ['0'] * 256
result = ''

def parse():
    global socket, field, result; row = 0;

    data = socket.recvuntil('<< ')

    if len(data) != 1203:
        data = data[-1203:]
        field = ['0'] * 256
        # print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    lines = data.split('\n')

    print data

    for line in lines:
        if '.' in line:
            for i, c in enumerate(line):
                col = (i - 4) / 4
                pos = 16 * row + col
                try:
                    if c == '.':
                        field[pos] = '0'
                    if c == 'O':
                        field[pos] = '2'
                    if c == 'X':
                        if field.count('1') == 0:
                            print '=============================================='

                        if field[pos] == '0':
                            if field.count('1') == 0:
                                result += chr(16 * col + row)
                                print result
                            print 'Computer move: ' + hex(col)[2:] + hex(row)[2:]
                            field[pos] = '1'
                except:
                    field = ['0'] * 256
                    print 'Exception?'
                    row = 1
            row += 1

def send_move(x, y):
    global socket, field;

    pos = 16 * y + x
    field[pos] = '2'

    trash = socket.recvuntil('<< ')
    print 'Your move: ' + hex(x)[2:] + hex(y)[2:]
    socket.send('%d %d\n' % (x, y))

def get_next_move():
    result = subprocess.check_output(['./gomoku', '-s', str().join(field), '-p', '2', '-t', '100', '-d', '8', '-l', '2000']).decode()
    temp = loads(result)

    return int(temp['result']['move_c']), int(temp['result']['move_r'])

for i in range(1000):
    parse()
    move = get_next_move()
    send_move(*move)
# parse()
