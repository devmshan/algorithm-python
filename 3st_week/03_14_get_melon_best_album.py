# 많이 많이 가장많이 나오면 정렬 써야 함

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# -> genre_array 에서 genre 별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어줄거다
# 특정 키 값에 대해서 value를 모아서 합쳐주고 싶다.
# 특정 키값은 아직 정해지지 않았다.
# dict = {}
# dict = {"classic": [500 +150+800], "pop": [600+2500]}
# -> dict 재생횟수로 정렬한다

# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# -> 많이 재생된 장르 별로 2곡을 넣어줄때, 많이 재생된 노래먼저 넣어줘야 한다.

# dict2 ={}
# dic2 = {"classic": [(0,500),(2,150),(3,800)], "pop": [(1,600),(4,2500)]}
# -> dict2 재생횟수로 정렬한다


def get_melon_best_album(genre_array, play_array):
    # 1. dict 에 장르별로 얼마나 재생횟수를 가지고 있는가
    # 2. dict 에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_song_count_dict = {} # { "장르": [(재생횟수, 인덱스), (재생횟수, 인덱스)], "장르2": [(재생횟수, 인덱스), (재생횟수, 인덱스)] }

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_song_count_dict[genre].append((play, i))
        else:
            genre_total_play_dict[genre] = play
            genre_song_count_dict[genre] = [(play, i)]
  
    #장르별로 가장 재생횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력하기
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda x: x[1], reverse=True) 

    result = []
    # for i in genre_total_play_dict:
    #     genre_song_count_dict[i[0]] = sorted(genre_song_count_dict[i[0]], key=lambda x: x[0], reverse=True)
    #     for j in range(min(len(genre_song_count_dict[i[0]]), 2)):
    #         result.append(genre_song_count_dict[i[0]][j][1])

    for genre, total_play in sorted_genre_play_array:
        sorted_genre_song_count_array = sorted(genre_song_count_dict[genre], key=lambda item: item[0], reverse=True)
        # 장르별로 2곡만 넣어라
        genre_song_count = 0
        for play, index in sorted_genre_song_count_array:
            result.append(index)
            genre_song_count += 1
            if genre_song_count == 2:
                break

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))