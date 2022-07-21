from function import *


cl = BE_Team(myToken="token_primary",
            myApp="IOS\t2.14.0\tIOS OS\t5.1.1")
owner = {'u9e985f41e819403811d01164abde9c77'}
protectkick = []
try :
    for zzz in owner:
        cl.findAndAddContactsByMid(zzz)
        cl.sendMessage('u9e985f41e819403811d01164abde9c77','ini midnya')
except :
    pass

def worker(op):
    try:
        if op.type in [13, 124]:
            if op.param2 in owner:
                cl.acceptChatInvitation(op.param1)
            else:
                cl.acceptChatInvitation(op.param1)
        if op.type in [19, 132]:
            if op.type in owner:
                if op.param2 not in owner:
                    cl.deleteOtherFromChat(op.param1, [op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoChat(op.param1, [op.param3])
            if op.param1 in protectkick:
                if op.param2 not in owner:
                    cl.deleteOtherFromChat(op.param1, [op.param2])

        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != cl.profile.mid: to = sender
            else: to = receiver

            if cmd == "ping":
                cl.sendMessage(to,'pong')

            if cmd == "speed":
                start = time.time()
                cl.sendMessage(to,'benchmark...')
                total = time.time()-start
                cl.sendMessage(to,str(total))
                
            if cmd == "protect kick on":
                if to not in protectkick:
                    protectkick.append(to)
                    cl.sendMessage(to, 'protect kick aktif')
                else:
                    cl.sendMessage(to, 'protect kick sudah aktif')
                    
            if cmd == "protect kick off":
                if to not in protectkick:
                    protectkick.append(to)
                    cl.sendMessage(to, 'protect kick tidak aktif')
                else:
                    cl.sendMessage(to, 'protect kick sudah tidak aktif')
                    
    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    while True:
        try:
            ops = cl.fetchOps()
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    cl.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    cl.individualRev = int(op.param1.split("\x1e")[0])
                cl.localRev = max(op.revision, cl.localRev)
                executor.submit(worker,op)
        except:
            pass
            
