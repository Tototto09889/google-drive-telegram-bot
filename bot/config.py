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
    START_MSG = "**Hai {}.**\n__Aku adalah Google Drive Uploader Bot.Kamu bisa menggunakanku untuk mengupload file / video dari direct link atau telegram ke Google Drive.__\n__Untuk informasi lebih lanjut, kamu bisa ketik perintah /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Aku bisa mengupload file dari direct link atau telegram ke google drive milikmu. Kamu hanya perlu login, kemudian kirim kepadaku file dari direct link atau dari telegram, dan aku akan menguploadnya.__\n\nAku punya fitur lainnya lhoo... ! Pengen tau ? Kalau emang pengen tau, kamu bisa klik tanda panah di bawah. Klik dengan hati-hati ya :).",
        
        f"**Login Google Drive**\n__Kirimkan padaku perintah /{BotCommands.Authorize[0]} dan kamu akan menerima URL, kunjungi URL tersebut dan kamu nanti akan mendapatkan kode, salin kode tersebut ke sini, selesai. Gunakan perintah /{BotCommands.Revoke[0]} untuk logout akun google drive milikmu.__\n\n**Catatan: Aku tidak akan menjawab perintah atau pesan apapun (kecuali kamu menggunakan perintah /{BotCommands.Authorize[0]}) untuk login akun milikmu.\nJadi, login itu penting!**",
        
        f"**Direct Links**\n__Kirimkan kepadaku file dari direct link, kemudian aku akan mendownloadnya dari serverku, dan menguploadnya ke akun google drive milikmu. kamu bisa mengganti nama filemu sebelum diupload. Caranya kirimkan padaku URLnya dan nama barunya dipisah dengan tanda ' | '.__\n\n**__Contoh:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__Untuk mengupload file dari telegram ke akun google drivemu, caranya cukup mudah. Teruskan file tersebut kepadaku, dan aku akan menguploadnya. Note: Kamu bisa spam file telegram sekaligus lho, tapi mungkin ada beberapa file yg gagal. Misalnya kamu mengirim 10 file sekaligus, mungkin 8 file yg berhasil dan 2 lainnya gagal. Kamu bisa mengirim ulang file yg gagal tersebut, dan aku akan menguploadnya.__\n\n**YouTube-DL Support**\n__Download file melalui youtube-dl.\nGunakan perintah /{BotCommands.Ytdl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder Untuk Tempat Upload File**\n__Kamu pengen upload file ke dalam__ **team drive** __milikmu ?\nGunakan perintah /{BotCommands.SetFolder[0]} (URL FOLDER) untuk mengatur tempat uploadmu.\nSemua file akan diupload ke dalam folder yang kamu pilih.__",
        
        f"**Delete Google Drive Files**\n__Menghapus file google drive. Gunakan perintah /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file.\nKamu juga dapat mengosongkan sampahmu dengan menggunakan perintah /{BotCommands.EmptyTrash[0]}\nNote: File akan dihapus secara permanen. Proses ini tidak bisa dibatalkan.\n\n**Copy Google Drive Files**\n__Yap, mengkloning  atau menyalin file google drive.\n__Gunakan perintah /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin file google drive orang ke google drive milikmu.__",
        
        "**Peraturan**\n__1. Jangan menyalin file/folder google drive dengan jumlah yang besar. Itu mungkin akan menyebabkan filemu rusak atau membuat bot hang.\n2. Jangan mengirim link macam zippyshare, mega, solidfiles, dkk. Gunakan @transload untuk mengubah mereka menjadi direct link. Saya merekomendasikan http://aws.rapidleech.gq/ untuk mengubah linkmu menjadi direct link.\n3. Tolong jangan menyalahgunakan layanan gratis ini.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @vcnmxd and @zxcxzcx**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded, coba lagi 24 jam mendatang :).__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder Tidak Ditemukan.**\n__File id - {} Tidak Ditemukan. Untuk memastikannya\'s ada dan dapat diakses dengan logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nPastikan URL Google Drivenya sudah dalam format yang benar."
    
    COPIED_SUCCESSFULLY = "✅ **Salin Berhasil.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Sedang Mengupload file...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Upload Berhasil.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Download Gagal**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Sedang Mendownload File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Kamu Sudah Login.**\n__Gunakan /revoke untuk logout akunmu yang sekarang.__\n__Kirimkan padaku direct link atau file telegram untuk kuupload ke google drivemu__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Gunakan perintah /{BotCommands.Authorize[0]}.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Login Akun Berhasil.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__Kode yang kamu kirim sudah invalid atau sudah digunakan. gunakan kode yang baru dengan mengunjungi Authorization URL__'
    
    AUTH_TEXT = "⛓️ **Untuk login akunmu, kamu bisa kunjungi [URL]({}) dan kirim kode tokennya ke sini.**\n__Caranya kunjungi URL > Berikan izin > kamu akan mendapatkan kode tokennya > salin kode tersebut > kirim ke sini__"
    
    DOWNLOAD_TG_FILE = "📥 **Sedang Mendownload File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder buat tempat upload sukses.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Berhasil Dihapus.**\n__Gunakan perintah__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __untuk mengaturnya ulang__.'
    
    CURRENT_PARENT = "🆔 **Custom Folder IDmu sekarang - {}**\n__Gunakan perintah__ ```/{} (Folder link)``` __untuk mengubahnya.__"
    
    REVOKED = f"🔓 **Berhasil  logout.**\n__Gunakan perintah /{BotCommands.Authorize[0]} untuk login kembali.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__Link yang kamu kirim bukan dari folder.__"
    
    CLONING = "🗂️ **Kloning Ke Google Drive...**\n__Link G-Drive - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Berhasil Menghapus File.**\n__Sekarang filemu sudah dihapus !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Tolong coba lagi nanti.__"
    
    EMPTY_TRASH = "🗑️🚮**Mengosongkan Sampah Berhasil !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
