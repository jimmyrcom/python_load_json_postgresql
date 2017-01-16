#!/usr/bin/python3
# Created by Jimmy Ruska under GPL 3 (JimmyR.com)

import psycopg2
import os,re,platform,sys,json

from subprocess import Popen, PIPE, STDOUT

def main():
    conn = psycopg2.connect("dbname={} user={} host={}".format(sys.argv[3],sys.argv[4],sys.argv[5]))
    cur = conn.cursor()
    i=0;

    with open(sys.argv[1], "r", 1) as ins:
        for line in ins:
            line1=''
            try:
                line = line.replace('\\u0000', '')
                p = Popen(['node', '-p'],1, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                line1 = p.communicate(input='JSON.stringify({})'.format(line.rstrip('\n')).encode('UTF-8'))[0].decode('UTF-8').rstrip('\n')
                cur.execute("Insert into {} (data) values (%s);".format(sys.argv[2]), (line1,))
            except:
                #print("fail: ",line)
                #print("out: ",line1)
                print("Unexpected error:", sys.exc_info()[0])
                #sys.exit()
                i=i+1
                print("Errors so far {}".format(i))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
