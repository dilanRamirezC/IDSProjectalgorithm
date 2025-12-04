import pyshark
import pandas as pd

pcap_file = 'Pruebas.pcap'  # Reemplaza con tu archivo real

cap = pyshark.FileCapture(pcap_file, use_json=True)
data = []

for pkt in cap:
    try:
        ip_src = pkt.ip.src
        ip_dst = pkt.ip.dst
        protocol = pkt.transport_layer or 'N/A'

        # Puertos
        src_port = pkt[protocol].srcport if protocol in pkt else 'N/A'
        dst_port = pkt[protocol].dstport if protocol in pkt else 'N/A'

        # TTL y longitud
        ttl = pkt.ip.ttl if hasattr(pkt.ip, 'ttl') else 'N/A'
        length = int(pkt.length)

        # TCP-specific features
        tcp_flags = pkt.tcp.flags if 'TCP' in pkt else 'N/A'
        tcp_window = pkt.tcp.window_size_value if 'TCP' in pkt else 'N/A'
        tcp_seq = pkt.tcp.seq if 'TCP' in pkt else 'N/A'
        tcp_ack = pkt.tcp.ack if 'TCP' in pkt else 'N/A'
        tcp_payload_len = pkt.tcp.len if 'TCP' in pkt else 'N/A'

        # Timestamp
        timestamp = pkt.sniff_time.isoformat()

        data.append({
            'ip_src': ip_src,
            'ip_dst': ip_dst,
            'src_port': src_port,
            'dst_port': dst_port,
            'protocol': protocol,
            'length': length,
            'ttl': ttl,
            'tcp_flags': tcp_flags,
            'tcp_window_size': tcp_window,
            'tcp_seq': tcp_seq,
            'tcp_ack': tcp_ack,
            'tcp_payload_len': tcp_payload_len,
            'timestamp': timestamp
        })

    except AttributeError:
        continue

cap.close()

# Guardar como CSV
df = pd.DataFrame(data)
df.to_csv('trafico_rico.csv', index=False)
print("Dataset enriquecido guardado como 'trafico_rico.csv'")
