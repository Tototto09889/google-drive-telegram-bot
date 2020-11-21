class config:
    BOT_TOKEN = "1480428484:AAEQ9hcgiEiYpxTDDCvio5NIHiXBIpExR9I"
    APP_ID = "2243484"
    API_HASH = "f4a1af6d7688c41138ef4b3d8c8d9baa"
    DATABASE_URL = "postgres://fsviyeazqyqlze:26a43d6a31455de234bf6283323ad2f92ed6bdb6c62ab6a962b95bb96f1cdf14@ec2-3-220-222-72.compute-1.amazonaws.com:5432/d14g2fauml4n2r"
    SUDO_USERS = "1104560929 1238661140" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/wibu12p"
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**Hai kawan {}.**\n__Aku adalah Google Drive Uploader Bot.Kamu bisa menggunakanku untuk mengupload file / video ke Google Drive dari direct link or Telegram.__\n__Untuk informasi lebih lanjut, kamu bisa ketik perintah /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Aku bisa mengupload file dari direct link or telegram to your Google Drive. Kamu hanya perlu login dengan akun google drivemu kemudian kirim kepadaku direct link or file dari telegram.__\n\nAku punya fitur lain lhoo... ! Pengen tau ? Kalau emang pengen tau, kamu bisa klik tanda panah di bawah. Klik dengan hati-hati ya :).",
        
        f"**Login Google Drive**\n__Kirimkan padaku perintah /{BotCommands.Authorize[0]} dan kamu akan menerima URL, kunjungi URL tersebut dan kamu nanti akan mendapatkan kode, salin kode tersebut ke sini, langkah-langkah selesai dan akunmu sudah login. Gunakan perintah /{BotCommands.Revoke[0]} untuk logout akun google drivemu.__\n\n**Catatan: Aku tidak akan menjawab perintah atau pesan apapun (kecuali kamu menggunakan perintah /{BotCommands.Authorize[0]}) untuk login akunmu.\nJadi, login itu penting!**",
        
        f"**Direct Links**\n__Kirimkan padaku file dari direct download link, kemudian aku akan mendownloadnya ke serverku, dan menguploadnya ke akun google drivemu. kamu bisa mengganti nama filemu sebelum diupload. Caranya kirimkan padaku URLnya dan nama barunya dipisah dengan tanda ' | '.__\n\n**__Contoh:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**File dari telegram**\n__Untuk mengupload file dari telegram ke akun google drivemu, caranya cukup mudah. Teruskan file tersebut kepadaku, dan aku akan menguploadnya. Note: Kamu bisa spam file telegram sekaligus lho. Tapi mungkin ada beberapa file yg gagal, misalnya kamu mengirim 10 file sekaligus, mungkin 8 yg berhasil dan 2 yg gagal. Kamu bisa mengirim ulang file yg gagal tersebut dan aku akan menguploadnya.__\n\n**YouTube-DL Support**\n__Download file melalui youtube-dl.\nGunakan perintah /{BotCommands.Ytdl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom folder untuk tempat file diupload**\n__Pengen upload filenya ke dalam__ **team drive** __ ?\nGunakan perintah /{BotCommands.SetFolder[0]} (URL FOLDER DARI GOOGLE DRIVEMU) untuk mengatur tempat uploadmu.\nSemua file akan diupload ke dalam folder yang kamu pilih.__",
        
        f"**Delete Google Drive Files**\n__Menghapus file google drive. Gunakan perintah /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file.\nKamu juga dapat mengosongkan sampahmu dengan menggunakan perintah /{BotCommands.EmptyTrash[0]}\nNote: File akan dihapus secara permanen. Proses ini tidak bisa dibatalkan.\n\n**Copy Google Drive Files**\n__Yap, mengkloning  atau menyalin file google drive.\n__Gunakan perintah /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin file google drive orang ke google drive milikmu.__",
        
        "**Peraturan dan tindakan pencegahan**\n__1. Jangan menyalin file/folder google drive dengan jumlah yang besar. Itu mungkin akan menyebabkan filemu rusak atau membuat bot hang.\n2. Jangan mengirim link macam zippyshare, mega, solidfiles, dkk. Gunakan @transload untuk mengubah mereka menjadi direct link. Saya merekomendasikan http://aws.rapidleech.gq/ untuk mengubah linkmu menjadi direct link.\n3. Tolong jangan menyalahgunakan layanan gratis ini.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @vcnmxd and @zxcxzcx**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
