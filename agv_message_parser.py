def parse_string(input_string):
    # 결과를 저장할 사전
    parsed_dict = {}
    
    # 이름과 값 쌍을 세미콜론으로 분리
    pairs = input_string.split('|')
    
    for pair in pairs:
        # 각 쌍에서 이름과 값을 콜론으로 분리
        val_name, values = pair.split(':')
        
        # 이름의 양쪽 공백을 제거
        val_name = val_name.strip()
        
        # 값을 쉼표로 분리하고 각 값의 양쪽 공백을 제거
        values_list = [value.strip() for value in values.split(',')]
        
        # 사전에 이름과 값 목록을 추가
        parsed_dict[val_name] = values_list
    
    return parsed_dict

# 예시 입력 문자열
input_string = "val_name : val1, val2, val3 | val_name2 : val1, val2"

# 파싱 함수 호출
parsed_result = parse_string(input_string)

# 결과 출력
print(parsed_result)


def process_name(val_name, values):
    match val_name:
        case "tar":
            return f"Processing {val_name} with values {values}"
        case "out":
            return f"Processing {val_name} with values {values}"
        case _:
            return f"Unknown val_name {val_name} with values {values}"