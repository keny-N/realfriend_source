<template>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <slot name="header">
          <h4 class="modal-title">タイトルタイトル</h4>
        </slot>
      </div>
      <div class="modal-body">
        <slot name="body"></slot>
      </div>
      <div class="modal-footer">
        <slot name="footer"></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
