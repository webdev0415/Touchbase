<template>
  <router-link style="text-decoration: none;" :to="to">
    <div class="uk-card uk-card-box uk-card-body uk-box-shadow-medium uk-border-rounded">
      <span class="uk-icon-forder uk-border-rounded">
        <span :data-uk-icon="iconString"></span>
      </span>
      <p>{{title}}</p>
    </div>
  </router-link>
</template>

<script>
export default {
	name: 'CategoryBox',
  props: ['title', 'icon', 'to'],
  data () {
    return {
      iconx: 'settings'
    }
  },
  computed: {
    iconString () {
      return `icon: ${this.icon}; ratio: 2`
    }
  }
}
</script>