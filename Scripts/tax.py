old_tax_regime = [
    (0, 2_50_000, 0.0),
    (2_50_001, 5_00_000, 0.05),
    (5_00_001, 10_00_000, 0.20),
    (10_00_001, ">", 0.30)
]


new_tax_regime = [
    (0, 3_00_000, 0.0),
    (3_00_001, 6_00_000, 0.05),
    (6_00_001, 9_00_000, 0.10),
    (9_00_001, 12_00_000, 0.15),
    (12_00_001, 15_00_000, 0.20),
    (15_00_001, ">", 0.30)
]
# 8 ==
# 0, 2.5 ===>  2.5-0 at 0% --> INC: 8-2.5=5.5
# 2.5, 5 ===> 5-2.5 at 5% --> INC: 5.5 -2.5=3
# 5, 10 ===> 10-5 at 20% --> INC: 3-(10-5) = -ve

def calculate_tax(income, slabs, new_regime=True, deductions=None):
    tax_payable = 0
    income -= 50_000 # standard deduction
    for start, end, rate in slabs:
        if end != ">": # max tab slab not reached
            slab_amt = end-start
            if income > slab_amt: # income is more than slab
                tax_payable += (end-start)*rate
                income -= slab_amt
            else: # this is the last slab you are part of
                tax_payable += (income)*rate
                print(f"After tax slab {start},{end} at rate: {rate} --> Tax: {tax_payable}, Income left: {income}")
                return tax_payable + (tax_payable*0.04) # 4% cess
        else: # max tax_slab reached
            tax_payable += (income)*rate
            print(f"After tax slab {start},{end} at rate: {rate} --> Tax: {tax_payable}, Income left: {income}")
            return tax_payable + (tax_payable*0.04) # 4% cess
        
        if income == 0:
            return tax_payable
        
        print(f"After tax slab {start},{end} at rate: {rate} --> Tax: {tax_payable}, Income left: {income}")
        

tax_payable = calculate_tax(
    income=17_45_000, 
    slabs=new_tax_regime,
    new_regime=True
)

print(tax_payable)
