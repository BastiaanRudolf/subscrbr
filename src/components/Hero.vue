<template>

    <div class="container mx-auto pt-40 lg:pt-52 2xl:pt-64 pb-16 lg:pb-20 xl:pb-28 2xl:pb-52 flex flex-col px-5 py-24 justify-center items-center max-w-7xl">
        <div class="w-full md:w-2/3 flex flex-col mb-6 text-center">
            <!-- Header text -->
            <h1 class="title-font tracking-tight font-extrabold text-2xl xs:text-3xl lg:text-4xl 2xl:text-6xl mb-4 text-gray-800">efefefefefefef Emails <span style="color: #6666FF;">Made Easy</span></h1>
            
            <!-- Sub text -->
            <p class="mb-8 leading-relaxed text-xs sm:text-sm lg:text-lg xl:text-xl 2xl:text-2xl">
                TESTETETStrgrgrg and earrrrrrsily collect & store emailaddresses with an Azure Static Web App.
                <br>
                <br>
                Try it orrrrrrut now. 👇
            </p>

            <!-- Form with button -->
            <div>
                <div class="flex w-full justify-center items-end">

                    <div class="relative mr-4 lg:w-full xl:w-1/2 w-2/4 md:w-full text-left">
                        <!-- Binding a placeholder from the Vuex store, just to show how it interacts -->
                        <input v-model="email" type="text" :placeholder="exampleEmail" name="hero-field" class="w-full bg-opacity-50 rounded placeholder-gray-600 placeholder-opacity-50 focus:ring-2 focus:bg-transparent border border-gray-300 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                    </div>
                    <button id="heroEmailSubscribe" @click="subscribeEmail" type="button" style="background: #6666FF;" class="flex-wrap relative my-auto disabled:opacity-50 text-sm xl:text-xl text-white justify-start rounded-full py-2 px-8 shadow-lg focus:outline-none focus:shadow-outline transform transition hover:shadow-xl hover:scale-105 duration-300 ease-in-out">Subscribe</button>
                </div>
                
                <!-- Response messages -->
                <p v-if="responseType === 'error'" class="text-xs text-red-500 mt-6 ml-1"> ❌ {{this.$store.state.responseMessage}} </p>
                <p v-if="responseType === 'success'" class="text-xs text-green-500 mt-6 ml-1"> ✅ {{this.$store.state.responseMessage}} </p>
            </div>
        </div>
    </div>

    <div data-collapse="medium" data-animation="default" data-duration="400" data-easing="ease" data-easing2="ease" role="banner" class="navigation w-nav">
    <div class="navigation-wrap">
      <a href="index.html" aria-current="page" class="logo-link w-nav-brand w--current"><img src="images/business-logo2x.png" width="108" alt="" class="logo-image"></a>
      <div class="menu">
        <nav role="navigation" class="navigation-items w-nav-menu">
          <a href="index.html" aria-current="page" class="navigation-item w-nav-link w--current">Home</a>
        </nav>
        <div class="menu-button w-nav-button"><img src="images/menu-icon_1menu-icon.png" width="22" alt="" class="menu-icon"></div>
      </div>
      <a href="#Big-Form" class="button cc-contact-us w-inline-block">
        <div>Jetzt testen</div>
      </a>
    </div>
  </div>
  <div id="Demo" class="section cc-store-home-wrap">
    <div class="intro-header">
      <div class="intro-content cc-homepage">
        <div class="intro-text">
          <div class="heading-jumbo">Automatische Immobilien Beschreibung</div>
          <div class="paragraph-bigger cc-bigger-white-light">Wir automatisieren Ihr Immobilienexposé. Nie wieder nervige Texte schreiben.<br></div>
        </div>
        <a href="#Big-Form" class="button cc-jumbo-button cc-jumbo-white w-inline-block">
          <div>Mehr erfahren</div>
        </a>
      </div>
    </div>
    <div class="container">
      <div class="home-content-wrap">
        <div class="div-block-2">
          <div class="div-block">
            <div class="home-section-wrap">
              <div>
                <div class="label cc-light">Immobilien Beschreibung</div>
                <h2 class="section-heading">Automatisiere deine Objekt Beschreibung</h2>
                <p class="paragraph-light">Fülle Die Parameter aus und bekomme eine vollwertige Objektbeschreibung deiner Immobilie.</p>
              </div>
            </div>
          </div>
          <div id="Big-Form" class="form-block w-form">
            <form id="email-form" name="email-form" data-name="Email Form" method="get"><select id="Objektart" name="field" data-name="Field" class="w-select">
                <option value="Wohnung">Wohnung</option>
                <option value="Einfamilienhaus">Einfamilienhaus</option>
                <option value="Doppelhaushälfte">Doppelhaushälfte</option>
              </select><select id="Erwerb-2" name="Erwerb" data-name="Erwerb" class="w-select">
                <option value="Zum Kauf">Zum Kauf</option>
                <option value="Zur Miete">Zur Miete</option>
              </select><input type="number" class="w-input" maxlength="256" name="Gr-e" data-name="Größe" placeholder="Größe (qm^2)" id="Groe-e"><input type="number" class="w-input" maxlength="256" name="B-der" data-name="Bäder" placeholder="Bäder" id="Baeder" required=""><input type="number" class="w-input" maxlength="256" name="Zimmer" data-name="Zimmer" placeholder="Zimmer" id="Zimmer-2" required=""><input type="number" class="w-input" maxlength="256" name="Stockwerk" data-name="Stockwerk" placeholder="Stockwerk" id="Stockwerk-2" required=""><input type="number" class="w-input" maxlength="256" name="Preis" data-name="Preis" placeholder="Preis" id="Preis-2" required=""><input type="number" class="w-input" maxlength="256" name="Baujahr" data-name="Baujahr" placeholder="Baujahr" id="Baujahr-2" required=""><input type="number" class="w-input" maxlength="256" name="Renovierung" data-name="Renovierung" placeholder="Letzte Renovierung" id="Renovierung-2" required=""><input type="text" class="w-input" maxlength="256" name="Stadt" data-name="Stadt" placeholder="Stadt" id="Stadt" required=""><label class="w-radio"><input type="radio" id="Keller" name="Keller" value="Keller" data-name="Keller" class="w-form-formradioinput w-radio-input"><span class="w-form-label" for="Keller">Keller</span></label><label class="w-radio"><input type="radio" id="Garten" name="Garten" value="Garten" data-name="Garten" class="w-form-formradioinput w-radio-input"><span class="w-form-label" for="Garten">Garten</span></label><label class="w-radio"><input type="radio" id="Balkon" name="Balkon" value="Balkon" data-name="Balkon" class="w-form-formradioinput w-radio-input"><span class="w-form-label" for="Balkon">Balkon</span></label><input type="submit" value="Submit" data-wait="Please wait..." class="w-button"></form>
            <div class="w-form-done">
              <div>Thank you! Your submission has been received!</div>
            </div>
            <div class="w-form-fail">
              <div>Oops! Something went wrong while submitting the form.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="motto-wrap">
        <div class="heading-jumbo-small">Hier erscheint gleich Ihre Objekt Beschreibung.</div>
      </div>
      <div class="divider"></div>
      <div class="about-story-wrap">
        <p id="Text-Output" class="text-output">Füllen Sie die obigen Felder aus und wir erstellen hier ihre einzigartige Immobilien Beschreibung - kostenlos.</p>
      </div>
      <div class="divider"></div>
    </div>
  </div>
  <div class="section cc-cta">
    <div class="container">
      <div class="cta-wrap">
        <div>
          <div class="cta-text">
            <div class="heading-jumbo-small">Automatisiere dein Exopsé.<br></div>
            <div class="paragraph-bigger cc-bigger-light">Today is the day to build the business of your dreams. Share your mission with the world — and blow your customers away.<br></div>
          </div>
          <a href="#Big-Form" class="button cc-jumbo-button w-inline-block">
            <div>Jetzt texten</div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="container">
      <div class="footer-wrap">
        <a href="#" target="_blank" class="webflow-link w-inline-block">
          <div class="paragraph-tiny">Powered by Angelos &amp; Tom</div>
        </a>
      </div>
    </div>
  </div>
  
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default ({
    data() {
        return {
            // This is the local version of the email,
            // this is mounted to the input
            email: '',
        }
    },
    computed: {
        ...mapGetters({
        // This is how you rename a getter, value is accessible
        // via exampleEmail now.
        exampleEmail: 'getExampleEmail',
        responseMsg: 'getResponseMessage',
        responseType: 'getResponseType'
        })
    },
    methods: {
        ...mapActions(["subscribe"]),
        subscribeEmail: function(){
            this.subscribe(this.email)
        },
    },
    watch: {
        responseMsg(newVal, oldVal) {
            return newVal, oldVal
        },
        responseType(newVal, oldVal) {
            return newVal, oldVal
        }
    }
})
</script>
