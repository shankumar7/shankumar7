import re

with open('/Users/shankumar/Desktop/shankumar7/README.md', 'r') as f:
    content = f.read()

tech_stack_old = """<br>
<b>Languages</b><br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" />
<img src="https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white" />

<br><br>
<b>Frontend & Frameworks</b><br>
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" />
<img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/Vue.js-35495e?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />

<br><br>
<b>Backend, Databases & Cloud</b><br>
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=firebase" />
<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
<img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />

<br><br>
<b>DevOps & Data Tools</b><br>
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Git-F05033?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />
<img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
<img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" />
<img src="https://img.shields.io/badge/Data_Analysis-FF9900?style=for-the-badge" />
<img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=Canva&logoColor=white" />
<img src="https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=Gradle&logoColor=white" />

<br><br>
<b>Hardware, IoT & Security</b><br>
<img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" />
<img src="https://img.shields.io/badge/Raspberry_Pi-C51A4A?style=for-the-badge&logo=raspberry-pi&logoColor=white" />
<img src="https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/AutoCAD-0696D7?style=for-the-badge&logo=autodesk&logoColor=white" />
<img src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white" />
<img src="https://img.shields.io/badge/Cybersecurity-000000?style=for-the-badge&logo=security&logoColor=white" />
<img src="https://img.shields.io/badge/ECC-0052CC?style=for-the-badge" />
<img src="https://img.shields.io/badge/TLS-238636?style=for-the-badge" />"""

tech_stack_new = """<br>
<b>Languages</b><br>
<img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/TypeScript-000000?style=for-the-badge&logo=typescript&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/JavaScript-000000?style=for-the-badge&logo=javascript&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Java-000000?style=for-the-badge&logo=openjdk&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/C%2B%2B-000000?style=for-the-badge&logo=c%2B%2B&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/C-000000?style=for-the-badge&logo=c&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/LaTeX-000000?style=for-the-badge&logo=latex&logoColor=C8A96E" />

<br><br>
<b>Frontend & Frameworks</b><br>
<img src="https://img.shields.io/badge/React-000000?style=for-the-badge&logo=react&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/React_Native-000000?style=for-the-badge&logo=react&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Vue.js-000000?style=for-the-badge&logo=vuedotjs&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/HTML5-000000?style=for-the-badge&logo=html5&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/CSS3-000000?style=for-the-badge&logo=css3&logoColor=C8A96E" />

<br><br>
<b>Backend, Databases & Cloud</b><br>
<img src="https://img.shields.io/badge/Node.js-000000?style=for-the-badge&logo=nodedotjs&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=mysql&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Firebase-000000?style=for-the-badge&logo=firebase&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Google_Cloud-000000?style=for-the-badge&logo=google-cloud&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=C8A96E" />

<br><br>
<b>DevOps & Data Tools</b><br>
<img src="https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Git-000000?style=for-the-badge&logo=git&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Postman-000000?style=for-the-badge&logo=postman&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Power_BI-000000?style=for-the-badge&logo=powerbi&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Tableau-000000?style=for-the-badge&logo=tableau&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Data_Analysis-000000?style=for-the-badge&logo=pandas&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Canva-000000?style=for-the-badge&logo=Canva&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Gradle-000000?style=for-the-badge&logo=Gradle&logoColor=C8A96E" />

<br><br>
<b>Hardware, IoT & Security</b><br>
<img src="https://img.shields.io/badge/Arduino-000000?style=for-the-badge&logo=Arduino&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Raspberry_Pi-000000?style=for-the-badge&logo=raspberry-pi&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/AutoCAD-000000?style=for-the-badge&logo=autodesk&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/MQTT-000000?style=for-the-badge&logo=mqtt&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/Cybersecurity-000000?style=for-the-badge&logo=security&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/ECC-000000?style=for-the-badge&logo=keybase&logoColor=C8A96E" />
<img src="https://img.shields.io/badge/TLS-000000?style=for-the-badge&logo=letsencrypt&logoColor=C8A96E" />"""

content = content.replace(tech_stack_new, tech_stack_old)


projects_old = """      <h3>AuthSphere</h3>
      <b>Self‑Hosted IoT Security Framework</b><br><br>
      <i>A patented, certificate‑driven solution that secures resource‑constrained IoT devices with automated onboarding and zero vendor lock‑in.</i><br><br>
      <img src="https://img.shields.io/badge/IoT-Security-red?style=for-the-badge" />
      <img src="https://img.shields.io/badge/PKI-Certificates-blue?style=for-the-badge" />
      <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
      <img src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white" />
      <img src="https://img.shields.io/badge/ECC-0052CC?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Patented-✓-green?style=for-the-badge" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>ClassCom</h3>
      <b>Academic Resource Gateway</b><br><br>
      <i>Full‑stack platform serving 210+ students with study materials, assignment tracking, and a Xerox print‑order pipeline generating ₹2.6L+ revenue.</i><br><br>
      <img src="https://img.shields.io/badge/Next.js-Full--Stack-black?style=for-the-badge&logo=next.js" />
      <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" />
      <img src="https://img.shields.io/badge/210%2B-Users-blue?style=for-the-badge" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <h3>DARKS Rakshak</h3>
      <b>Disaster Response Drone System</b><br><br>
      <i>Dual‑drone architecture where a carrier deploys an autonomous reconnaissance unit, improving survivor detection in flood rescues.</i><br><br>
      <img src="https://img.shields.io/badge/Autonomous-Drones-orange?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Disaster-Response-red?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/Computer-Vision-yellow?style=for-the-badge" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>Snippet Scanner</h3>
      <b>Static Code Security Analyzer</b><br><br>
      <i>Rapid tool that flags OWASP Top 10 vulnerabilities in code snippets and offers remediation guidance.</i><br><br>
      <img src="https://img.shields.io/badge/OWASP-Top10-purple?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Static-Analysis-blue?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/Security-000000?style=for-the-badge&logo=security&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <h3>Arogya Drishti</h3>
      <b>Secure Hospital Management System</b><br><br>
      <i>End‑to‑end platform built with IoT security and data integrity at its core.</i><br><br>
      <img src="https://img.shields.io/badge/HealthTech-IoT-teal?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Secure--by--Design-✓-green?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Management-005C84?style=for-the-badge" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>Tomato Sorter &amp; TECHBOW</h3>
      <b>Computer Vision &amp; Human‑Robot Interaction</b><br><br>
      <i>Vision pipeline for automated produce sorting, paired with HRI research for intuitive interaction.</i><br><br>
      <img src="https://img.shields.io/badge/Computer-Vision-yellow?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Robotics-HRI-gray?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Automation-blue?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Agricultural-Tech-green?style=for-the-badge" />"""

projects_new = """      <h3>AuthSphere</h3>
      <b>Self‑Hosted IoT Security Framework</b><br>
      <blockquote><i>A patented, certificate‑driven solution that secures resource‑constrained IoT devices with automated onboarding and zero vendor lock‑in.</i></blockquote><br>
      <img src="https://img.shields.io/badge/IoT_Security-000000?style=for-the-badge&logo=shield&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/PKI_Certificates-000000?style=for-the-badge&logo=letsencrypt&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/C%2B%2B-000000?style=for-the-badge&logo=c%2B%2B&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/MQTT-000000?style=for-the-badge&logo=mqtt&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/ECC-000000?style=for-the-badge&logo=keybase&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Patented-000000?style=for-the-badge&logo=awesomelists&logoColor=C8A96E" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>ClassCom</h3>
      <b>Academic Resource Gateway</b><br>
      <blockquote><i>Full‑stack platform serving 210+ students with study materials, assignment tracking, and a Xerox print‑order pipeline generating ₹2.6L+ revenue.</i></blockquote><br>
      <img src="https://img.shields.io/badge/Next.js_Full_Stack-000000?style=for-the-badge&logo=next.js&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Node.js-000000?style=for-the-badge&logo=nodedotjs&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=mysql&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/210%2B_Users-000000?style=for-the-badge&logo=users&logoColor=C8A96E" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <h3>DARKS Rakshak</h3>
      <b>Disaster Response Drone System</b><br>
      <blockquote><i>Dual‑drone architecture where a carrier deploys an autonomous reconnaissance unit, improving survivor detection in flood rescues.</i></blockquote><br>
      <img src="https://img.shields.io/badge/Autonomous_Drones-000000?style=for-the-badge&logo=drone&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Disaster_Response-000000?style=for-the-badge&logo=firstaid&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Computer_Vision-000000?style=for-the-badge&logo=opencv&logoColor=C8A96E" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>Snippet Scanner</h3>
      <b>Static Code Security Analyzer</b><br>
      <blockquote><i>Rapid tool that flags OWASP Top 10 vulnerabilities in code snippets and offers remediation guidance.</i></blockquote><br>
      <img src="https://img.shields.io/badge/OWASP_Top10-000000?style=for-the-badge&logo=owasp&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Static_Analysis-000000?style=for-the-badge&logo=sonarqube&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Security-000000?style=for-the-badge&logo=security&logoColor=C8A96E" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <h3>Arogya Drishti</h3>
      <b>Secure Hospital Management System</b><br>
      <blockquote><i>End‑to‑end platform built with IoT security and data integrity at its core.</i></blockquote><br>
      <img src="https://img.shields.io/badge/HealthTech_IoT-000000?style=for-the-badge&logo=health&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Secure_by_Design-000000?style=for-the-badge&logo=shield&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Management-000000?style=for-the-badge&logo=trello&logoColor=C8A96E" />
    </td>
    <td width="50%" valign="top" align="center">
      <h3>Tomato Sorter &amp; TECHBOW</h3>
      <b>Computer Vision &amp; Human‑Robot Interaction</b><br>
      <blockquote><i>Vision pipeline for automated produce sorting, paired with HRI research for intuitive interaction.</i></blockquote><br>
      <img src="https://img.shields.io/badge/Computer_Vision-000000?style=for-the-badge&logo=opencv&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Robotics_HRI-000000?style=for-the-badge&logo=robot&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Automation-000000?style=for-the-badge&logo=arduino&logoColor=C8A96E" />
      <img src="https://img.shields.io/badge/Agricultural_Tech-000000?style=for-the-badge&logo=leaf&logoColor=C8A96E" />"""

content = content.replace(projects_new, projects_old)

with open('/Users/shankumar/Desktop/shankumar7/README.md', 'w') as f:
    f.write(content)

print("Reverted successfully")
