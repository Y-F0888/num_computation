import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_CEILING, ROUND_FLOOR, ROUND_DOWN, ROUND_UP, getcontext

# Decimalの計算精度を設定（この例では中間計算の精度に影響）

test_values = [2.5, 2.51, 2.49, 3.5, 3.51, 3.49, -2.5, -2.51, -2.49, -3.5, -3.51, -3.49]

print("\n--- Decimal (10進数) の丸め ---")
print("Decimal型は浮動小数点誤差がなく、丸め方式を明示的に指定できる")
print("quantize(Decimal('1'), rounding=...) で整数に丸める")

# 丸め方式
rounding_modes = {
    "ROUND_UP": ROUND_UP,               # 0から離れる方向へ丸める
    "ROUND_DOWN": ROUND_DOWN,           # 0へ近づく方向へ丸める
    "ROUND_HALF_UP": ROUND_HALF_UP,     
    "ROUND_HALF_DOWN": ROUND_HALF_DOWN, # 0.5は0から遠ざかる方に丸める
    "ROUND_HALF_EVEN": ROUND_HALF_EVEN, # 近い値に丸める
    "ROUND_CEILING": ROUND_CEILING,     # 正の無限大方向へ丸める 
    "ROUND_FLOOR": ROUND_FLOOR          # 負の無限大方向へ丸める
}

print(f"{'Value':<10}", end="")
for name in rounding_modes.keys():
    print(f"{name:<18}", end="")
print("\n" + "-" * (10 + 18 * len(rounding_modes)))

for val_float in test_values:
    val_dec = Decimal(str(val_float)) # floatの文字列表現からDecimalを生成することで、floatの誤差をDecimalに持ち込まない
    print(f"{val_dec:<10}", end="")
    for mode_name, mode_value in rounding_modes.items():
        # quantize(Decimal('1'), ...) は小数点以下を丸めて整数にする
        # Decimal('1') は丸め先の桁数指定（この場合、1の位まで）
        rounded_val = val_dec.quantize(Decimal('1'), rounding=mode_value)
        print(f"{rounded_val:<18}", end="")
    print()

print("\n--- Decimal の丸め方式の違いによる影響のまとめ ---")
print("特に .5 の値で違いが顕著になる")
print("  - ROUND_UP: 常に0から離れる方向へ丸める。例: 2.1->3, -2.1->-3")
print("  - ROUND_DOWN: 常に0へ近づく方向へ丸める。例: 2.1->2, -2.1->-2 (int()と同じ挙動)")
print("  - ROUND_HALF_UP (一般的な四捨五入): 0.5は切り上げ")
print("  - ROUND_HALF_DOWN: 0.5は切り捨て（0から遠ざかる方向）")
print("  - ROUND_HALF_EVEN (銀行家の丸め): 0.5は最も近い偶数へ。例: 2.5->2, 3.5->4")
print("  - ROUND_CEILING: 常に正の無限大方向へ丸める。例: 2.1->3, -2.1->-2")
print("  - ROUND_FLOOR: 常に負の無限大方向へ丸める。例: 2.1->2, -2.1->-3")
