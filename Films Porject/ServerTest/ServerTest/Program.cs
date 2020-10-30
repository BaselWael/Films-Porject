using System;
using System.Text;
using System.Net;
using System.Net.Sockets;

namespace ServerTest
{
    class Program
    {
        static void Main(string[] args)
        {
            recv recvv = new recv();
            recvv.rcv();
            string location_ = recvv.GetData();
            Console.WriteLine(location_);
            recvv.resetdata();
            recvv.rcv();
            string filmname_ = recvv.GetData();
            Console.WriteLine(filmname_);
            //string filmname_ = "C:\\Users\\Basola\\Desktop\\Projects\\Films Porject\\Iron Man 3.Torrent";
            //string location_ = "C:\\Users\\Basola\\Desktop\\Projects\\Films Porject";
            int x = 0;
            while(x==0)
            {


                try
                {
                    torrent.download(filmname: filmname_, location: location_).GetAwaiter().GetResult();
                }
                catch
                {
                    
                    torrent.download(filmname: location_, location: filmname_).GetAwaiter().GetResult();
                }

                Console.WriteLine("Done");
            } 
        }
    }
}
