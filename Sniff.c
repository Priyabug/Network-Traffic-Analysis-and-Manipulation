#include <stdlib.h>
#include <stdio.h>
#include <pcap.h>

void got_packet(u_char *args, const struct pcap_pkthdr *header,
        const u_char *packet)
{
  printf("Got a packet\n");
}

int main()
{
  pcap_t *handle;
  char errbuf[PCAP_ERRBUF_SIZE];
  struct bpf_program fp;
  char filter_exp[] = "icmp";
  bpf_u_int32 net;

  // Step 1: Open live pcap session on NIC with name enp0s3
  handle = pcap_open_live("enp0s3", BUFSIZ, 1, 1000, errbuf); 
