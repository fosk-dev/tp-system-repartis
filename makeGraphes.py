#!/usr/bin/python3.6

import sys
import os
import time
import matplotlib.pyplot as plt

print("""```    ********     *********    ********    ********* "
```    *       *    *           *       *    *        *
```    *       *    *           *       *    *         *
```    *       *    *           *       *    *          *
```    ********     *********   *********    *           *
```    *       *    *           *       *    *          *
```    *       *    *           *       *    *         *
```    *       *    *           *       *    *        *
```    *       *    *********   *       *    *********    BY KSOF   
```""")

print("""Show graphs""")

def run():
    # # Server log
    # with open('send_log_file/sd_log.txt') as file_log_sd:
    with open(sd_file) as file_log_sd:
        lines0 = file_log_sd.readlines()
        x_sd = [line.split()[0] for line in lines0]
        y_sd = [line.split()[1] for line in lines0]

    # Retreat data x send
    x_sd_bn = []
    for i in range(len(x_sd)):
        x_sd_bn.append(float(x_sd[i]))

    # Retreat data y send
    y_sd_bn = []
    for i in range(len(y_sd)):
        y_sd_bn.append(float(y_sd[i]))

    #### Get receive information from log file
    with open(rcv_file) as file_log_rcv:
        lines1 = file_log_rcv.readlines()
        x_rcv = [line1.split()[0] for line1 in lines1]
        y_rcv = [line1.split()[1] for line1 in lines1]

    # Retreat data x receive
    x_rcv_bn = []
    for i in range(len(x_rcv)):
        x_rcv_bn.append(float(x_rcv[i]))

    # Retreat data y receive
    y_rcv_bn = []
    for i in range(len(y_rcv)):
        y_rcv_bn.append(float(y_rcv[i]))

    if forWho == "server":
        plt.plot(x_sd_bn, y_sd_bn, label="Server send")
        plt.plot(x_rcv_bn, y_rcv_bn, color="green", label="Server receive")
    elif forWho == "client":
        plt.plot(x_sd_bn, y_sd_bn, label="Client send")
        plt.plot(x_rcv_bn, y_rcv_bn, color="green", label="Client receive")
    
    # plt.axis([0, 1, 0, 10000])
    # plt.axes.set_frame_on(False) 
    # axes.yaxis.tick_left()
    # axes.xaxis.set_visible(False)
    # plt.axes.spines['top'].set_visible(False)

    plt.xlabel('time')
    plt.ylabel('bw')

    if etat == "s":
        plt.title('Graphe slow network!')
    elif etat == "f":
        plt.title('Graphe fast network!')
    
    plt.legend()
    plt.get_current_fig_manager().window.setGeometry(0, 0, 800, 800)
    plt.show()


if __name__ == '__main__':
    sd_file = sys.argv[1]
    rcv_file = sys.argv[2]
    forWho = sys.argv[3]
    etat = sys.argv[4]
    run()