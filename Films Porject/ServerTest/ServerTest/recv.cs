using System;
using System.Collections.Generic;
using System.Net;
using System.Text;
using System.Net.Sockets;

namespace ServerTest
{
     class recv
     {
        string data;
        public void rcv()
        {
            try
            {
                IP Myip = new IP();
                Myip.IPAdress_();
                string ip = Myip.Get();
                IPAddress ipAd = IPAddress.Parse(ip);
                TcpListener mylist = new TcpListener(ipAd, 8080);
                mylist.Start();
                Console.WriteLine("Server is runing at port 8080");
                Console.WriteLine($"The local End point is : {mylist.LocalEndpoint}");
                Console.WriteLine("Waiting for connection....");
                Socket s = mylist.AcceptSocket();
                Console.WriteLine($"Connection Accepted from {s.RemoteEndPoint}");
                byte[] b = new byte[100];
                int k = s.Receive(b);
                Console.WriteLine("Recieved...");
                 
                for (int i = 0; i < k; i++)
                {
                    //Console.Write(Convert.ToChar(b[i]));
                    data += Convert.ToChar(b[i]);
                }

                ASCIIEncoding asen = new ASCIIEncoding();
                s.Send(asen.GetBytes("Data Recieved"));
                Console.WriteLine("\nSent Acknowledgement");
                s.Close();
                mylist.Stop();
                s.Close();
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error... {e.StackTrace}");
            }
           
        }
        public string GetData()
        {
            return data;
        }
        public void resetdata()
        {
            data = "";
        }
        

     }
    
}
