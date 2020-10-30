using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using MonoTorrent;
using MonoTorrent.Client;

namespace ServerTest
{
    class torrent
    {
        
        public async static Task download(string filmname,string location)
        {
            Senddata sd = new Senddata();

            var t = Torrent.Load(location);
            var c = new ClientEngine();
            var m = new TorrentManager(t, filmname);

            await c.Register(m);
            await c.    StartAllAsync();

            while (m.State != TorrentState.Stopped && m.State != TorrentState.Paused)
            {
                string progrs = Convert.ToString(m.Progress);
                sd.send(data:progrs);
                Console.WriteLine($"Torrent is: {m.Progress}%");
                string speed = Convert.ToString(c.TotalDownloadSpeed);
                Console.WriteLine($"Download Speed: {c.TotalDownloadSpeed/1024}");
                sd.send(data: speed);
                Thread.Sleep(1000);
  
                if (m.Progress == 100.0)
                {
                    // If we want to stop a torrent, or the engine for whatever reason, we call engine.Stop()
                    // A tracker update *must* be performed before the engine is shut down, so you must
                    // wait for the waithandle to become signaled before continuing with the complete
                    // shutdown of your client. Otherwise stats will not get reported correctly.
                    await c.StopAllAsync();
                    return;
                }
            }
        }
    }
}
