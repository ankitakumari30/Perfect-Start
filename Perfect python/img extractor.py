import requests
from bs4 import BeautifulSoup

urls = ['https://igzy.com/',
'https://igzy.com/careers/',
'https://igzy.com/cloud-security-solutions/',
'https://igzy.com/logistics-case-study/',
'https://igzy.com/industrial-automation/',
'https://igzy.com/office-security/',
'https://igzy.com/qsr-case-study/',
'https://igzy.com/remote-warehousing/',
'https://igzy.com/retail-case-study/',
'https://igzy.com/security-surveillance-system/',
'https://igzy.com/smart-enterprise-solutions/',
'https://igzy.com/use-cases/',
'https://igzy.com/thermal-scanner/',
'https://igzy.com/become-a-partner/',
'https://igzy.com/igzy-checklist/',
'https://igzy.com/privacy-policy/',
'https://igzy.com/cloud-kitchen-iot-solutions/',
'https://igzy.com/sme-solutions/',
'https://igzy.com/terms-conditions/',
'https://igzy.com/about-us/',
'https://igzy.com/retail-solution-sme/',
'https://igzy.com/salon-surveillance-platform/',
'https://igzy.com/small-server-room-solutions/',
'https://igzy.com/smart-cloud-kitchen-security-solutions/',
'https://igzy.com/video-surveillance-solution-for-educational-institutions/',
'https://igzy.com/automotive-services-security-solutions/',
'https://igzy.com/hospitality-surveillance-solutions/',
'https://igzy.com/use-cases/employee-monitoring/',
'https://igzy.com/use-cases/energy-management/',
'https://igzy.com/use-cases/access-control-system/',
'https://igzy.com/use-cases/fire-safety/',
'https://igzy.com/iot-based-solutions-case-studies/',
'https://igzy.com/brochures/',
'https://igzy.com/solution-for-home/',
'https://igzy.com/iot-platform/',
'https://igzy.com/ultimate-cctv-camera-guide/',
'https://igzy.com/senior-care-solutions/',
'https://igzy.com/brochures/solutions-for-warehousing-and-logistics/',
'https://igzy.com/brochures/transforming-with-iot-quick-service-restaurants/',
'https://igzy.com/brochures/solution-for-retail/',
'https://igzy.com/brochures/igzy-for-banking-financial-services/',
'https://igzy.com/whitepapers/transforming-quick-service-restaurants-with-iot/',
'https://igzy.com/whitepapers/implementation-of-iot-in-warehouses/',
'https://igzy.com/whitepapers/transforming-retail-with-iot/',
'https://igzy.com/whitepapers/sense-analyse-and-act/',
'https://igzy.com/whitepapers/',
'https://igzy.com/patient-monitoring-system-for-clinics-and-diagnostic-centers/',
'https://igzy.com/whitepapers/transforming-bfsi-with-iot/',
'https://igzy.com/contact-us/',
'https://igzy.com/use-cases/patient-monitoring-solution/',
'https://igzy.com/use-cases/cloud-camera-solutions-for-industries/',
'https://igzy.com/use-cases/video-retrieval-and-retention/',
'https://igzy.com/cloud-storage-vs-local-storage/',
'https://igzy.com/use-cases/perimeter-intrusion-detection-system/',
'https://igzy.com/video-analytics/',
'https://igzy.com/restaurants-video-surveillance-system/',
'https://igzy.com/enterprise-security-solutions-platform/',
'https://igzy.com/bank-atm-security-system/',
'https://igzy.com/warehouse-security-system/',
'https://igzy.com/solution-for-business/',
'https://igzy.com/intelligent-industrial-security-solution/',
'https://igzy.com/iot-based-solutions-case-studies/how-we-assisted-a-leading-apparel-brand-to-improve-operations-and-enhance-profitability/',
'https://igzy.com/iot-based-solutions-case-studies/how-we-assisted-a-leading-telecom-company-attain-improved-efficiency-and-security/',
'https://igzy.com/iot-based-solutions-case-studies/how-our-iot-surveillance-solutions-helped-improve-security-at-a-leading-warehousing-company/',
'https://igzy.com/iot-based-solutions-case-studies/how-our-iot-solutions-helped-improve-efficiency-at-a-leading-logistics-company/',
'https://igzy.com/iot-based-solutions-case-studies/how-we-assisted-a-renowned-quick-service-restaurant-chain-attain-improved-efficiency/',
'https://igzy.com/smart-retail-solutions/',
'https://igzy.com/smart-factory-solutions/',
'https://igzy.com/healthcare-security-system/',
'https://igzy.com/smart-living-solutions/',
'https://igzy.com/ebooks/',
'https://igzy.com/bfsi/',
'https://igzy.com/cloudcctv/',
'https://igzy.com/iot-based-solutions-case-studies/cloud-based-surveillance-helped-bfsi-leader/',
'https://igzy.com/warehouse-2-2/']


for url in urls:
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text)
  for heading in soup.find_all(["img"]):
      print(f"'{url}', '{heading['src']}'")
#
# open file in write mode
# with open(r'img.txt', 'w') as fp:
#     for url in urls:
#         reqs = requests.get(url)
#         soup = BeautifulSoup(reqs.text)
#         for heading in soup.find_all(["img"]):
#             fp.write(f"'{url}', '{heading['src']}'")
            # print(f"'{url}', '{heading['src']}'")
        # fp.write("%s\n")
      
      
      
      
      