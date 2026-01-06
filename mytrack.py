#!/usr/bin/env python3

import requests
import os
import sys

# لوجو الأداة بتصميم ASCII احترافي
logo = """
\033[1;36m
  _____             _     _____ _____  
 |  __ \           | |   |_   _|  __ \ 
 | |__) |_ _ _ __ ___ | |_    | | | |__) |
 |  ___/ _` | '__/ _ \| __|   | | |  ___/ 
 | |  | (_| | | | (_) | |_   _| |_| |     
 |_|   \__,_|_|  \___/ \__| |_____|_|     
                                          
 \033[1;33m[+] Professional IP Tracker & OS Detector
 \033[1;33m[+] Bypass: Ping Scan Enabled (-Pn)
 \033[1;32m[+] Developed by: Your Name (Parrot OS)
\033[0m"""

def track_pro():
    os.system('clear')
    print(logo)
    
    target = input("\n\033[1;32m[?] Enter Target IP (or leave empty for yours): \033[0m")
    
    # جلب البيانات الجغرافية
    url = f"http://ip-api.com/json/{target}?fields=status,message,country,regionName,city,lat,lon,timezone,isp,as,query"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            ip_addr = data['query']
            print(f"\n\033[1;34m" + "─"*45)
            print(f" 🛰️  DETAILED REPORT FOR: {ip_addr}")
            print("─"*45 + "\033[0m")
            
            print(f"📍 Location:    {data.get('city')}, {data.get('regionName')}, {data.get('country')}")
            print(f"🌐 ISP:         {data.get('isp')}")
            print(f"⏰ Timezone:    {data.get('timezone')}")
            
            # رابط الخريطة
            maps_url = f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
            print(f"🗺️  Google Maps: \033[4;35m{maps_url}\033[0m")
            
            # فحص نظام التشغيل باستخدام Nmap المطور
            print(f"\n\033[1;33m[!] Scanning for OS & Ports (Bypassing Firewall)... \033[0m")
            print("\033[1;30m" + "─"*45 + "\033[0m")
            
            # تم إضافة -Pn لتجاوز مشكلة "Host seems down" 
            # وتم إضافة --max-retries لزيادة سرعة الفحص
            os.system(f"sudo nmap -Pn -O -F --max-retries 1 {ip_addr}")
            
            print("\033[1;30m" + "─"*45 + "\033[0m")
            
            # خيار حفظ التقرير
            save = input("\n\033[1;32m[?] Save this report to a file? (y/n): \033[0m")
            if save.lower() == 'y':
                with open(f"report_{ip_addr}.txt", "w") as f:
                    f.write(f"IP Report: {ip_addr}\nLocation: {data.get('city')}, {data.get('country')}\nMaps: {maps_url}\n")
                print(f"\033[1;32m[+] Report saved: report_{ip_addr}.txt\033[0m")
                
        else:
            print(f"\033[1;31m[!] Error: {data.get('message')}\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Connection Error: {e}\033[0m")

if __name__ == "__main__":
    try:
        track_pro()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Exiting...\033[0m")
        sys.exit()
