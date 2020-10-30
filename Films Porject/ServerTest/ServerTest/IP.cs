using System;
using System.Collections.Generic;
using System.Net;
using System.Text;

namespace ServerTest
{
    class IP
    {
        string data = "";
        public void IPAdress_()
        {
            string strHostName = Dns.GetHostName();
            IPHostEntry ipEntry = Dns.GetHostEntry(strHostName);
            IPAddress[] addr = ipEntry.AddressList;
        }
        public string Get()
        {
            return "127.0.0.1";
        }
    }
}
