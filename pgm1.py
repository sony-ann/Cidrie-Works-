with open ('sample_logs.txt', 'r') as f:
    for i in f:
        if "ERROR" in i:
            time = i.split(']')[0].strip('[')
            error = i.split('ERROR:')[1].strip()
            print(f"{time},{error}")
