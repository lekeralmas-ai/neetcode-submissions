class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = list()
        for email in emails:
            i = 0
            corrected_email = ""
            while i < len(email):
                if email[i] == '.' and '@' not in corrected_email:
                    i += 1
                elif email[i] == '+':
                    while email[i] != '@':
                        i +=1
                else:
                    corrected_email += email[i]
                    i+=1
                
            if corrected_email not in res:
                res.append(corrected_email)
        return len(res)
