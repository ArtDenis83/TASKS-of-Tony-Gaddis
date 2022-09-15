# Task 12. Stock Transaction Program
# Use f-string because they are faster and more convenient

# Set value:
# 2000 shares, $40 for 1 share
shares_buy = 2000 * 40

# 3% commission
buy_com = shares_buy * 0.03

# 2000 shares, 42.75 for 1 share
shares_sell = 2000 * 42.75

# 3% commission
sell_com = shares_sell * 0.03

# Calculate
balance = shares_sell - (buy_com + sell_com)
total_profit = balance - shares_buy

# Return result
print(f"Total cost of buy shares: $ {shares_buy:.2f}")
print(f"Total cost of buy commission: $ {buy_com:.2f}")
print(f"Total cost of sell shares: $ {shares_sell:.2f}")
print(f"Total cost of sell commission: $ {sell_com:.2f}")
print(f"Actual balance: $ {balance:.2f}")
print(f"Total profit of deal: $ {total_profit:.2f}")
