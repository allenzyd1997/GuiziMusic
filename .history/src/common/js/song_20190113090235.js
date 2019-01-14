import {getLyric} from 'api'

export default class Song {
    constructor({id, mid, singer, name, albunm, duration, image, url}) {
        this.id = id
        this.singer = singer
        this.name = name
        this.album = album 
        this.duration = duration
        this.image = image
        this.url = url 
    }
}

export function createSong(musicData) {
    return new Song({
        id: musicData.song_id,
        singer: filterSinger(musicData.singer),
        name: musicData.song_name,
        album: musicData.album_id,
        duration: musicData.interval,
        lyric: musicData.lrc_url,
        song: musicData.song_url,
        image: musicData.pic_url
    })
}