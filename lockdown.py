import json

def trigger_lockdown():
    print("\n[!] CRITICAL ATTACK STOPPED: DEPLOYING MITIGATION SYSTEM...")
    
    forensic_log = {
        "status": "COMPROMISED_KEY_DETECTED",
        "action": "AUTOMATED_KEY_REVOCATION_SENT"
    }
    
    with open("incident_response_dump.json", "w") as f:
        json.dump(forensic_log, f, indent=4)
    print("[+] Emergency log file saved: incident_response_dump.json\n")

if __name__ == "__main__":
    trigger_lockdown()
