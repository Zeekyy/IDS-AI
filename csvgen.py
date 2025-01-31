import pandas as pd
import numpy as np

num_rows = 5000

np.random.seed(42)
data = {
    'duration': np.random.randint(0, 1000, num_rows),
    'protocol_type': np.random.choice(['tcp', 'udp', 'icmp'], num_rows),
    'service': np.random.choice(['http', 'ftp', 'smtp', 'telnet', 'private'], num_rows),
    'flag': np.random.choice(['SF', 'S0', 'REJ', 'RSTO'], num_rows),
    'src_bytes': np.random.randint(0, 10000, num_rows),
    'dst_bytes': np.random.randint(0, 10000, num_rows),
    'land': np.random.randint(0, 2, num_rows),
    'wrong_fragment': np.random.randint(0, 3, num_rows),
    'urgent': np.random.randint(0, 3, num_rows),
    'hot': np.random.randint(0, 3, num_rows),
    'num_failed_logins': np.random.randint(0, 5, num_rows),
    'logged_in': np.random.randint(0, 2, num_rows),
    'num_compromised': np.random.randint(0, 5, num_rows),
    'root_shell': np.random.randint(0, 2, num_rows),
    'su_attempted': np.random.randint(0, 2, num_rows),
    'num_root': np.random.randint(0, 5, num_rows),
    'num_file_creations': np.random.randint(0, 5, num_rows),
    'num_shells': np.random.randint(0, 2, num_rows),
    'num_access_files': np.random.randint(0, 5, num_rows),
    'num_outbound_cmds': np.random.randint(0, 5, num_rows),
    'is_host_login': np.random.randint(0, 2, num_rows),
    'is_guest_login': np.random.randint(0, 2, num_rows),
    'count': np.random.randint(0, 500, num_rows),
    'srv_count': np.random.randint(0, 500, num_rows),
    'serror_rate': np.random.random(num_rows),
    'srv_serror_rate': np.random.random(num_rows),
    'rerror_rate': np.random.random(num_rows),
    'srv_rerror_rate': np.random.random(num_rows),
    'same_srv_rate': np.random.random(num_rows),
    'diff_srv_rate': np.random.random(num_rows),
    'srv_diff_host_rate': np.random.random(num_rows),
    'dst_host_count': np.random.randint(0, 500, num_rows),
    'dst_host_srv_count': np.random.randint(0, 500, num_rows),
    'dst_host_same_srv_rate': np.random.random(num_rows),
    'dst_host_diff_srv_rate': np.random.random(num_rows),
    'dst_host_same_src_port_rate': np.random.random(num_rows),
    'dst_host_srv_diff_host_rate': np.random.random(num_rows),
    'dst_host_serror_rate': np.random.random(num_rows),
    'dst_host_srv_serror_rate': np.random.random(num_rows),
    'dst_host_rerror_rate': np.random.random(num_rows),
    'dst_host_srv_rerror_rate': np.random.random(num_rows),
    'label': np.zeros(num_rows)  # 0 for normal, 1 for malicious
}

malicious_indices = np.random.choice(num_rows, int(num_rows * 0.2), replace=False)
for idx in malicious_indices:
    data['num_failed_logins'][idx] = np.random.randint(5, 10)
    data['count'][idx] = np.random.randint(500, 1000)
    data['src_bytes'][idx] = np.random.randint(10000, 20000)
    data['dst_bytes'][idx] = np.random.randint(10000, 20000)
    data['serror_rate'][idx] = np.random.uniform(0.5, 1.0)
    data['srv_serror_rate'][idx] = np.random.uniform(0.5, 1.0)
    data['rerror_rate'][idx] = np.random.uniform(0.5, 1.0)
    data['srv_rerror_rate'][idx] = np.random.uniform(0.5, 1.0)
    data['label'][idx] = 1  

df = pd.DataFrame(data)
df.to_csv('training_data.csv', index=False)
print("Training CSV file generated.")