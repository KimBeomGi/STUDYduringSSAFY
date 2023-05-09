<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{pickMenu}}</p>
    <br><br><br>
    <h1>로또를 뽑아보자</h1>
    <button @click="pickLotto">Pick Lotto</button>
    
  </div>
</template>

<script>
export default {
  name:'TheLotto',
  data(){
    return{
      foodMenu : [
        '김밥', '돼지국밥', '라면', '피자', '짜장면', '우동', '오므라이스', '치킨', '샌드위치', '샐러드',
        '떡볶이', '족발', '보쌈', '라면사리', '만두', '굶어', '새우튀김', '양념치킨', '햄버거', '고기국수',
        '쌀국수', '회', '부대찌개', '된장찌개', '제육볶음', '비빔밥', '죽', '해장국', '미역국', '김치찌개',
        '오징어볶음', '닭갈비', '소고기볶음', '갈비찜', '꼬치어', '파스타', '스테이크', '초밥', '회덮밥', '냉면',
        '콩나물국밥', '닭볶음탕', '게장', '꽃게탕', '곱창', '막창', '치즈돈까스', '감자탕', '김치전', '파전',
        '계란찜', '갈비탕', '매운탕', '어묵국', '굴국밥', '철판볶음밥', '짬뽕', '팟타이', '반계탕', '쭈꾸미볶음',
        '닭강정', '수육', '보리밥', '청국장찌개', '냉모밀', '오므라이스', '불고기', '스팸볶음', '꼬막찜', '김치볶음밥',
        '간장게장', '칼국수', '동그랑땡', '닭꼬치', '갈치구이', '곰탕', '피자',
        '치킨마요', '쭈꾸미볶음밥', '김치볶음밥', '만두국', '꽃게', '새우볶음밥', '육개장', '청국장', '비빔냉면', '된장불고기',
        '콩나물불고기', '김치찜', '닭칼국수', '돈까스', '초계국수', '파스타'
      ],
      pickMenu : ''
    }
  },
  methods: {
    pickLunch(){
      const randomIndex = Math.floor(Math.random()*this.foodMenu.length);
      this.pickMenu = this.foodMenu[randomIndex]
      
    },
    pickLotto(){
      this.$router.push({name:'lotto'})
    }
  }
}
</script>

<style>

</style>