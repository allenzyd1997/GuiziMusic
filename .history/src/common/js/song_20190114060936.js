

export default class Song {
    constructor({id, singer, name, album, duration, image, song, lyric}) {
        this.id = id
        this.singer = singer
        this.name = name
        this.album = album 
        this.duration = duration
        this.image = image
        this.song = song
        this.lyric = lyric 
    }
}

export function createSong(musicData) {
    return new Song({
        id: musicData.song_id,
        singer: musicData.singer_id,
        name: musicData.song_name,
        album: musicData.album_id,
        duration: format(musicData.duration),
        lyric: musicData.lrc_url,
        song: musicData.song_url,
        image: musicData.pic_url
    })
}

function format(s){
    var t;
    if(s > -1){
        var min = Math.floor(s/60) % 60;
        var sec = s % 60;
        if(min < 10){t += "0";}
        t = min + ":";
        if(sec < 10){t += "0";}
        t += sec.toFixed(0);
    }
    return t
}