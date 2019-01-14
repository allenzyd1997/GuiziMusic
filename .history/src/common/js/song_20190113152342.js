

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
        duration: musicData.interval,
        lyric: musicData.lrc_url,
        song: musicData.song_url,
        image: musicData.pic_url
    })
}