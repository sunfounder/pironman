import subprocess

'''
Use subprocess.popen instead of os.popen to avoid some errors
'''

# Return CPU temperature as a character string 
def getCPUtemperature():
    res = subprocess.check_output('vcgencmd measure_temp',shell=True).decode()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list                                       
# Index 0: total RAM                                                               
# Index 1: used RAM                                                                 
# Index 2: free RAM 
def getRAMinfo():
    ram = subprocess.check_output('free |grep Mem',shell=True).decode()
    return(ram.split()[1:4])
        
# Return % of CPU used as a character string
def getCPUuse(): 
    cmd = "top -bn1 |awk '/Cpu\(s\):/ {print $8}'"
    CPU_usage = subprocess.check_output(cmd,shell=True) .decode()
    CPU_usage = round(100 - float(CPU_usage),1)
    return CPU_usage

# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                         
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used
def getDiskSpace():
    disk = subprocess.check_output("df -h |grep /dev/root",shell=True).decode()
    return(disk.split()[1:5])

# IP address
def getIP():
    wlan0 = subprocess.check_output("ifconfig wlan0 |awk '/inet/'|awk 'NR==1 {print $2}'",shell=True).decode().strip('\n')
    eth0 = subprocess.check_output("ifconfig eth0 |awk '/inet/'|awk 'NR==1 {print $2}'",shell=True).decode().strip('\n')
    if wlan0 == '':
        wlan0 = None
    if eth0 == '':
        eth0 = None

    return wlan0,eth0



if __name__ == '__main__':
    # CPU informatiom
    CPU_temp = getCPUtemperature()
    CPU_usage = getCPUuse()
    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1024,1)
    RAM_used = round(int(RAM_stats[1]) / 1024,1)
    RAM_free = round(int(RAM_stats[2]) / 1024,1)
    RAM_usage = round(RAM_used/RAM_total*100,1)
    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]
    # IP
    wlan0,eth0 = getIP()
    
    print('')
    print('CPU Temperature = %s \'C' % CPU_temp)
    print('CPU Use = %s %%'%CPU_usage)
    print('')
    print('RAM Total = %s MB'%RAM_total)
    print('RAM Used = %s MB'%RAM_used)
    print('RAM Free = %s MB'%RAM_free)
    print('RAM Usage = %s %%'%RAM_usage)
    print('')  
    print('DISK Total Space = '+str(DISK_total))
    print('DISK Used Space = '+str(DISK_used))
    print('DISK Used Percentage = '+str(DISK_perc))   
    print('wlan0 : %s'%wlan0)
    print('eth0 : %s'%eth0)
    


 