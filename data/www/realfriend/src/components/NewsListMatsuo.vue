<template>
<!--  <h2>小さいフォントくん</h2>-->
  <div>
    <div class="overflow-auto">
      <ul>
        <li v-for="item in list">
          {{item.title}}
        </li>
      </ul>
    </div>

    <input type="text" id="newsadd">
    <button @click="add">追加</button>
  </div>
</template>

<script>
    export default {
        name: "ListMT",
        data() {
          return{
            list: [
              {title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く"}
            ],
            modal: false
          }
        },
      methods: {
          add() {
            this.list.push({title:document.getElementById("newsadd").value})
          },
          newsDetailsOpen() {
            this.modal = true
          },
          newsDetailsClose() {
            this.modal = false
          }
      }
    }
</script>

<style scoped>
  .overflow-auto{
    width: 100%;
    height: 30vh;
    margin: auto auto;
    overflow-x: visible;
  }
  ul,li{
    width: 100%;
  }
  li{
    list-style: none;
    margin-left: -20px;
  }
</style>
