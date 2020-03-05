# Ahmed Kareem Dimah - - IBN testing-Project / Simulating Intent-based networking with multiple network Vendors

# STEPS 
  1- Featching datasets for each network service.
  
  2- Building machine learning algorithems to find the optimum one that will be used later:
  
    A- Supervised learning 
    B- Unsupervised learning 
    C- Re-inforcment learning
    
  3- Connecting the network with the module that got optimum learning rate from our datasets from step 1.
  
  4- Testing our module with multiple failures senarios. 

# Toplogy has been attached to the master/       

# The network is currently run (but not limited to) below network vendors: 
  1- CISCO -IOS XE/CSR1000v, V16.07.01
  
  2- Nokia -TiMOS/7750 SR7, R14.01 
  
  3- Cumulus - Linux/Linux, V3.7
  
  4- Juniper (Future update)
  
  5- Arista (Future update)
  
  6- Huawei (Future update)
  
  7- HP (Future update)
  
  8- CISCO -IOS XR (Future update)
  
  9- Mellanox (future update)
  
# Current Running Configuration: 
  # IGP:
    1- OSPF (CISCO, KIA)
    2- ISIS (NOKIA)
    3- EIGRP(CISCO)
    4- EGP (Cumulus, NOKIA)
    
  # Transporters:  
    1- Segment-routing (NOKIA)
    2- GRE (NOKIA, CISCO, Cumulus)
    3- MPLS (LDP) (NOKIA, CISCO)
    4- EVPN (Cumulus, NOKIA)
    5- MPLS (RSVP) (NOKIA)
    6- MP-BGP (NOKIA)
    7- MVPN (NOKIA)
    8- PIM (NOKIA)
    9- MPLS (mLDP) (NOKIA)
    10- MPLS (RSVP P2MP) (NOKIA)
    
  - (Protoections: ECMP, TI/LFA, LFA remote, LFA local, graceful_restart, fitlers, Fast-reroute (Facility,one-to-one) )
  
  # Services:
    1- Xconnect (CISCO)
    2- VPLS (NOKIA, CISCO, Cumulus)
    3- EPIPE (NOKIA)
    4- VRF L3VPN (NOKIA, CISCO, Cumulus) 
    5- VPWS by BGP AD&Signaling (NOKIA, CISCO)
    6- VRRP (NOKIA, CISCO)
    7- BNG (broadband network gateway) (NOKIA)
    8- L2>L3 VPN (NOKIA, CISCO)
    9- VxLAN L2VPN (NOKIA, Cumulus) 
    10- VxLAN L3VPN (NOKIA, Cumulus)
    11- DMVPN (CISCO)
    12- VRF Inter-AS vpn model-C (NOKAI)
    13- NG-MVPN with MPLS (NOKIA)
    14- CSC (Carrier support Carrier) VPN (NOKIA)
    15- ESM over MPLS (NOKIA)
    16- MC-LAG (NOKIA, CISCO)
    17- EVPN-MPLS interconnect for EVPN-VXLAN VPLS
    18- MVPN inter-AS vpn model-B

  # Features Enabled [each specify per a test link connection]
    1- BGP FlowSpec for IPv4
    2- QoS traffic shaping and separation(Voice,Data)
    3- MPLS Link Coloring
    4- BGP Multipath 
    5- BGP Best-path-selection 
    6- VRF BGP eiBGP multipath load_balance 
    7- OSPF Sham link
    8- MPLS (IGP-shortcut, BGP-shortcut)
    9- BGP Route Leaking 
    10- ISIS Link_Bundling
    11- OSPF,ISIS Traffic engineering
    12- Segment-routing and LDP interworking 
    13- MPLS (LDP and RSVP interworking)
    14- LDP FEC to BGP Label Route interworking (RFC 3701)
    15- Seamless MPLS
    16- MPLS SRLG 
    17- Traffic leaking from VPRN to GRT
    
    -- GMPLS (MPLS-TP) (Future update)

  # Automation/Machine Learning/ Artificial intelligence/ Analyzing
    1- Sandbox (Dockers) / BaseMachine (GPU/NVIDIA Tesla K4)
      1.1- Python3.7 (Libraries: netmiko, Nampy, Sklearn, multiprocessing, threading, SMTPlib, xlsxwriter, Tensoflow, Panda, Pymango, MYSQLdb)
      1.2- Database [MongoDB, MySQL]
