class HoGiaDinh:
    def __init__(self, maho, chuho, diachi, mkhoi):
        self.maho = maho
        self.chuho = chuho
        self.diachi = diachi
        self.mkhoi = mkhoi
        self.total_amount = self.calculate_total_amount()

    def calculate_water_fee(self):
        tier_prices = [150, 200, 250, 300]
        tiers = [10, 10, 10]  
        water_fee = 0
        remaining_mkhoi = self.mkhoi

        for i, mkhois in enumerate(tiers + [remaining_mkhoi]):
            if remaining_mkhoi <= 0:
                break
            to_charge = min(remaining_mkhoi, mkhois if i < len(tiers) else remaining_mkhoi)
            water_fee += to_charge * tier_prices[min(i, len(tier_prices) - 1)]
            remaining_mkhoi -= to_charge

        return water_fee

    def calculate_total_amount(self):
        water_fee = self.calculate_water_fee()
        vat = water_fee * 0.10
        return water_fee + vat

    def __str__(self):
        return f"{self.maho} | {self.chuho} | {self.diachi} | {self.mkhoi} m3 | {self.total_amount:.2f} VNĐ"


def write_to_file(households, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Ma ho | Ten chu ho | Dia chi | So khoi | Tong tien\n") 
        for household in households:
            file.write(str(household) + '\n')

households = [
    HoGiaDinh("001", "Nguyễn Kim Hoàng", "Lộc Ninh", 40),
    HoGiaDinh("002", "Đào Duy Thanh", "Lộc Ninh", 45),
    HoGiaDinh("003", "Huỳnh Thị Đào", "Lộc Ninh", 55),
]

for household in households:
    print(household)

file_path = 'TienNuoc.txt'
write_to_file(households, file_path)

file_path  
