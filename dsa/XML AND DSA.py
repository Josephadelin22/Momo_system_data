import xml.etree.ElementTree as ET
import json
import re
import time

def parse_sms_body(body):
    result = {}
    match_received = re.search(r'You have received\s*([\d,]+)\s*RWF from (.+?) \((.*?)\).*at ([\d-]+ [\d:]+)', body)
    match_payment = re.search(r'payment of\s*([\d,]+)\s*RWF to (.+?) .*completed at ([\d-]+ [\d:]+)', body)
    match_txid = re.search(r'TxId[:\. ]*([\d]+)', body)
    match_finid = re.search(r'Financial Transaction Id[:\. ]*([\d]+)', body)

    if match_received:
        result['transaction_type'] = 'received'
        result['amount'] = match_received.group(1).replace(',', '')
        result['sender'] = match_received.group(2)
        result['receiver'] = 'Your Account'
        result['timestamp'] = match_received.group(4)
        result['transaction_id'] = match_finid.group(1) if match_finid else None
    elif match_payment:
        result['transaction_type'] = 'payment'
        result['amount'] = match_payment.group(1).replace(',', '')
        result['receiver'] = match_payment.group(2)
        result['timestamp'] = match_payment.group(3)
        result['transaction_id'] = match_txid.group(1) if match_txid else None

    return result

tree = ET.parse(r"C:\Users\asade\Downloads\modified_sms_v2 (1).xml")
root = tree.getroot()

sms_list = []

for sms in root.findall('sms'):
    sms_id = sms.get('date')  # using date as unique id if no explicit id
    address = sms.get('address')
    body = sms.get('body')
    parsed_body = parse_sms_body(body)
    sms_dict = {
        "id": sms_id,
        "service": address,
        "body": body
    }
    sms_dict.update(parsed_body)
    sms_list.append(sms_dict)

# Save to JSON
with open(r"C:\Users\asade\Downloads\sms_transactions2.json", "w") as f:
    f.write(json.dumps(sms_list, indent=2))

print("Parsed and extracted core details from SMS records.")

# --- DSA Comparison ---

if len(sms_list) >= 20:
    sample = sms_list[:20]
    search_id = sample[10]['id']

    def linear_search(tx_list, search_id):
        for tx in tx_list:
            if tx['id'] == search_id:
                return tx
        return None

    # Linear Search Timing
    start_linear = time.time()
    res_linear = linear_search(sample, search_id)
    end_linear = time.time()
    linear_duration = end_linear - start_linear

    # Dictionary Lookup Timing
    tx_dict = {tx['id']: tx for tx in sample}
    start_dict = time.time()
    res_dict = tx_dict.get(search_id)
    end_dict = time.time()
    dict_duration = end_dict - start_dict

    print(f"\nLinear search time: {linear_duration:.8f}s")
    print(f"Dictionary lookup time: {dict_duration:.8f}s")
    print("Linear search result (id={}): {}".format(search_id, res_linear))
    print("Dictionary lookup result (id={}): {}".format(search_id, res_dict))
else:
    print("Not enough records for DSA timing comparison.")
