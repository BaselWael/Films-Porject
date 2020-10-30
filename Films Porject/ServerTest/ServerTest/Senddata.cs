using System;
using System.Collections.Generic;
using System.Net;
using System.Text;
using System.Net.Sockets;


namespace ServerTest
{
    class Senddata
    {
        public void send(string data)
        {
            IP Myip = new IP();
            Myip.IPAdress_();
            string ip = Myip.Get();
            IPAddress host = IPAddress.Parse(ip);
            IPEndPoint hostep = new IPEndPoint(host, 8080);
            Socket sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            try
            {
                sock.Connect(hostep);
            }
            catch (SocketException e)
            {
                Console.WriteLine("Problem connecting to host");
                Console.WriteLine(e.ToString());
                sock.Close();
                return;
            }
            try
            {
                sock.Send(Encoding.ASCII.GetBytes(data));
            }
            catch (SocketException e)
            {
                Console.WriteLine("Problem sending data");
                Console.WriteLine(e.ToString());
                sock.Close();
                return;
            }
            sock.Close();
        }
    }
}
