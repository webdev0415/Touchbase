<template>
  <div>
    <section class="tm-margin-large-top tm-faq">
      <div class="uk-container">
        <h1 class="uk-margin-medium-bottom uk-heading-hero">Frequently Asked Questions</h1>

        <hr class="uk-margin-remove" />

        <ModernList :items="settings" />

        <ArticleComponent title="Text6" id="article-1">
          <p>Text7</p>
          <p>Text8</p>
        </ArticleComponent>

        <ArticleComponent title="Text9" id="article-2">
          <p>Text10</p>
        </ArticleComponent>

        <ArticleComponent title="Text11" id="article-3">
          <p>Text12</p>
        </ArticleComponent>

        <ArticleComponent title="Text13" id="article-4">
          <p>Text14</p>
        </ArticleComponent>

        <ArticleComponent title="Text15" id="article-5">
          <p>Text16</p>
        </ArticleComponent>

				<ArticleComponent title="Text17" id="article-6">
          <p>Text18</p>
        </ArticleComponent>

				<ArticleComponent title="Text19" id="article-7">
          <p>Text20</p>
        </ArticleComponent>
      </div>
    </section>
    <ContactUs />
  </div>
</template>

<script>
import ContactUs from "@/components/support/ContactUs"
import ModernList from "@/components/support/ModernList"
import ArticleComponent from "@/components/support/ArticleComponent"

export default {
  name: "FAQ",
  components: {
    ContactUs,
    ModernList,
    ArticleComponent
  },
  data() {
    return {
      settings: [
        { title: "Text1", ref: "#article-1" },
        { title: "Text2", ref: "#article-2" },
        { title: "Text3", ref: "#article-3" },
        { title: "Text4", ref: "#article-4" },
        { title: "Text5", ref: "#article-5" },
        { title: "Text6", ref: "#article-6" },
        { title: "Text7", ref: "#article-7" }
      ]
    };
  }
};
</script>