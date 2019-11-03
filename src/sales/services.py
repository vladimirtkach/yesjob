# class PhoneNormalizer:
#     def __init__(self, raw_phone):

def normalize_phone(raw_phone):
    phone = raw_phone.split(",")[0]
    phone = "".join(i for i in phone if i.isnumeric())

    if len(phone) < 9 or len(phone) > 12:
        return None
    if len(phone) == 9 and any(phone.startswith(ext) for ext in ["39", "68", "97", "50", "95", "63", "73", "91", "94",
                                                                 "67", "96", "98", "66", "99", "93", "89", "92"]):
        return "380" + phone
    if len(phone) == 10 and any(phone.startswith(ext) for ext in ["039", "068", "097", "050", "095", "063", "073", "091", "094",
                                                                 "067", "096", "098", "066", "099", "093", "089", "092"]):
        return "38" + phone
    if len(phone) == 11 and any(phone.startswith(ext) for ext in ["8039", "8068", "8097", "8050", "8095", "8063", "8073", "8091", "8094",
                                                                 "8067", "8096", "8098", "8066", "8099", "8093", "8089", "8092"]):
        return "3" + phone
    if len(phone) == 12 and any(phone.startswith(ext) for ext in ["38039", "38068", "38097", "38050", "38095", "38063", "38073", "38091", "38094",
                                                                 "38067", "38096", "38098", "38066", "38099", "38093", "38089", "38092"]):
        return phone

    if phone.startswith("48") and len(phone) == 11:
        return phone

