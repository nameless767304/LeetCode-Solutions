class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            local_number = "".join(c for c in s if c.isdigit())
            
            if len(local_number) > 10:
                country_code = "+" + "*" * (len(local_number) - 10) + "-"
            else:
                country_code = ""
            local_number = "***-***-" + local_number[-4:]


            return country_code + local_number






